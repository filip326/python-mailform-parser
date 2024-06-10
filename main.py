# IMAP (TLS) connection
import imaplib
import email
import os

from getpass import getpass


def parse(line: str, key: str) -> str:
    if key not in line:
        return None

    while not line.startswith(key):
        line = line[1:]

    # remove the substring
    line = line[len(key) :]
    line = line.split("\n")[0]
    line = line.removesuffix("\r")

    # remove until =
    if "=" not in line:
        return None
    while not line.startswith("="):
        line = line[1:]
    # remove the =
    line = line[1:]
    # trim
    line = line.strip()

    return line


# IMAP server
imapHost = input("IMAP Server: ")
imapPort = input("IMAP Port: ")
imapUsername = input("IMAP Username: ")
imapPassword = getpass("IMAP Password: ")

# Connect to IMAP server
imapClient = imaplib.IMAP4_SSL(imapHost, imapPort)

imapClient.login(imapUsername, imapPassword)

# Get a list of all mailboxes / directories
status, mailboxes = imapClient.list()

mailboxToFetch = '"INBOX/VL-Wahl: Klassensprecher"'

response, emailCount = imapClient.select(mailboxToFetch)

print(f"Fount {emailCount[0]} emails in {mailboxToFetch}")

# fetch all emails
status, emailIds = imapClient.search(None, "ALL")

emailIds: bytearray = emailIds[0].split()

results = {}

for i, emailId in enumerate(emailIds):
    # fetch the email
    status, emailData = imapClient.fetch(emailId, "(RFC822)")

    # print from and subject header of the email
    emailMessage = email.message_from_bytes(emailData[0][1])

    for part in emailMessage.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            text = body.decode("utf-8")

            results[i] = {}

            results[i]["From"] = emailMessage["From"]

            if ";Jahrgang" in text:
                results[i]["Jahrgang"] = parse(text, ";Jahrgang")
            if ";Klasse" in text:
                results[i]["Klasse"] = parse(text, ";Klasse")
            if ";Klassensprecher" in text:
                results[i]["Klassensprecher"] = parse(text, ";Klassensprecher")
            if ";Stellvertreter" in text:
                results[i]["Stellvertreter"] = parse(text, ";Stellvertreter")

print(results)
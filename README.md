# Mailform Parser

This is an imap-based script to make polls over email. I used it to get information about who the class representatives of different classes in my school are, by asking the teachers to answer me a mail.

In this mail, I've put the fields I need, in this case `Jahrgang` (=Year level), `Klasse` (Class / Group), `Klassensprecher` (representative), `Stellvertreter` (deputy). The semicolon `;` is used to prevent other uses of the key words to mistaken as the form input. The parser takes the value between the equals sign `=` after the key and the next new line `\n` or `\r\n` as the value.

## Usage
1. write the participants of your poll a nice mail
   In this mail, include your questions (make it easier by keeping the questions short keywords), prefixed with a semicolon `;` and suffixed with a equals sign `=`. Ask the participants to write their answers between the equalssign and the next line.
2. send the mail
3. get the responses and put them into a single folder
4. adjust this script to your needs: You need to change the folder name (line 48) to how you named your own folder. For me, it was the name of the poll. You also want to adjust the fields that will be parsed in lines 77+
5. run the script and check the results. You propably will need to fix some mistakes, since people mostly are not able to give you machine readable data
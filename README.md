# EmailDLer
Send a link in an email and download to a remote pc

This simple python script will read through a given inbox for a subject line (the default is 'DownloadThis', but it can be 
changed.) and follows the url in the body of the email and downloads the file. This works with music, images, etc.

To get up and running, just modify the following parts of the script:

imapthing -- default mail server is imap.mail.yahoo.com, this can be changed.

Add a username(email address) and password to the email account

Optional -- change the subject line to a custom line

Finally, part two moves the file to a more convienient place, this can be modified or omitted.

#Download files sent to email

import pyzmail
import imapclient
import requests
import time
import shutil

currentTime = time.time()
#create imap object -- modify to preferred email
imapthing = imapclient.IMAPClient('imap.mail.yahoo.com', ssl =True)

#add the username and password for the email account:
username = ''
passwd = ''

#log into the server
imapthing.login(username, passwd)

#select inbox to search
imapthing.select_folder('Inbox')

#search the subject line for 'DownloadThis'
uids = imapthing.search([u'SUBJECT', u'DownloadThis'])

#get raw data message to be decoded by pyzmail
rawMessages = imapthing.fetch(uids, ['BODY[]'])

#only executes if there are messages to process
if uids:

    for num in uids:
        #convert raw messages, get the body(the dl link), and download the file
        #the link.replace() line gets rid of any escape characters that sneak in
        message = pyzmail.PyzMessage.factory(rawMessages[num][b'BODY[]'])
        link = message.text_part.get_payload().decode(message.text_part.charset)
        link = link.replace('\r\n','')
        r = requests.get(str(link))

        #opens a file and saves to disk
        nowsec = time.time()
        fullTime = time.localtime(nowsec)
        fileName = time.strftime('%b%d-%Y-%I_%M_%S%p', fullTime)

        #write download to file named as the current date/time
        writeF = open(fileName, 'wb')

        for chunk in r.iter_content(100000):
            writeF.write(chunk)

        writeF.close()

        #Delete emails
        imapthing.delete_messages(num)
        imapthing.expunge()


#Part two: move files from /home/User to /home/User/Downloads/EmailDL using shutil
#If you dont need this part and/or are happy with where the file gets downloaded 
#or if this part straightup doesn't work, feel free to comment/delete/omit it.

#Again, only executes if there was a message processed
if uids:

    src = '/home/User/' + str(fileName)
    dst = '/home/User/Downloads/EmailDL/'

    shutil.move(src, dst)

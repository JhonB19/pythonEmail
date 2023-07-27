import imaplib
import email


# credenciales de la cuenta
username = "jhonfredyrivera@yahoo.com"
password = "BaldurSoftCol26"

imap_server = "imap.mail.yahoo.com"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)


import imaplib
 # Connect to the IMAP server
imap_server = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
 # Login to your Yahoo email account
username = 'your_username'
password = 'your_password'
imap_server.login(username, password)
 # Select the mailbox you want to work with (e.g., 'INBOX')
mailbox = 'INBOX'
imap_server.select(mailbox)
 # Fetch the list of email IDs in the mailbox
status, response = imap_server.search(None, 'ALL')
email_ids = response[0].split()
 # Iterate over the email IDs and fetch the corresponding messages
for email_id in email_ids:
    # Fetch the email message by ID
    status, response = imap_server.fetch(email_id, '(RFC822)')
    raw_email = response[0][1]
     # Process the raw email data as needed
    # For example, you can use the email library to parse the email
 # Logout and close the connection
imap_server.logout()
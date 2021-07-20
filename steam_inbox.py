import imaplib
import email

host = 'imap.gmail.com'
username = 'kunforever16@gmail.com'
password = 'additya007'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")


_, search_data = mail.search(None, 'UNSEEN')

mail_list = search_data[0].split()
latest = mail_list[-1]
_, data = mail.fetch(latest, '(RFC822)')
_, b = data[0]
email_message = email.message_from_bytes(b)
# print(email_message)
# print(email_message, file=open('mail.txt', 'w'))
x = str(email_message)
a = x.split('Here is the Steam Guard code you need to login to account kunforever16:</td>\r\n\t\t\t\t</tr>\r\n\t\t\t</table>\r\n\t\t\t\t\t\t<table width="100%" border="0" cellspacing="0" cellpadding="0">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td class="pb-70 mpb-50" style="padding-bottom: 70px;">\r\n\t\t\t\t\t\t<table width="100%" border="0" cellspacing="0" cellpadding="0"bgcolor="#17191c">\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td class="py-30 px-56" style="padding-top: 30px; padding-bottom: 30px; padding-left: 56px; padding-right: 56px;">\r\n\t\t\t\t\t\t\t\t\t<table width="100%" border="0" cellspacing="0" cellpadding="0">\r\n\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t<td class="title-48 c-blue1 fw-b a-center" style="font-size:48px; line-height:52px; font-family:\'Motiva Sans\', Helvetica, Arial, sans-serif; color:#3a9aed; font-weight:bold; text-align:center;">\r\n\t\t\t\t\t\t\t\t\t\t\t\t')
b = a[1]
code = b[1:6]
print(code)

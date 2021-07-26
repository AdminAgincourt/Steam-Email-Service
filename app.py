import streamlit as st
import time
import imaplib
import email

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
b_str = str(b)
b_last = b_str.split('Here is the Steam Guard code you need to login to account kunforever16:')
code = b_last[1][8:13]

############ Streamlit Code ###############

st.title("Steam Access Code")

st.write("The code will appear only once. Please do not refresh.")

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        st.write("You will shortly receive the code")
        time.sleep(1)
        time_sec -= 1

    st.write("Steam code to access the account is: ")
    st.write(code)

countdown(5)
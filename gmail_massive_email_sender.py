#!/usr/bin/python
# -*- coding: utf-8 -*-

# gmail_massive_email_sender

#Made by Julián Caro Linares-jcarolinares@gmail.com

#LICENSE: CC-BY-SA

#Based on the examples of:
# www.pythondiario.com

import os

#Email and server libraries
from email.mime.text import MIMEText
from smtplib import SMTP

#Config  library
import ConfigParser


class gmail_account:
    def new(self,user,password):
        self.password=str(password)
        self.user=str(user)
    def get_user(self):
        return self.user
    def get_password(self):
        return self.password

class email:
    def new(self,from_address, to_address,subject, message):
        self.from_address=str(from_address)
        self.to_address=str(to_address)
        self.subject=str(subject)
        self.message=str(message)
    def get_from_address(self):
        return self.from_address
    def get_to_address(self):
        return self.to_address
    def get_subject(self):
        return self.subject
    def get_message(self):
        return self.message

def main():

    #User data
    print '[+] Reading config file...'
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('./config')])

    user=gmail_account()
    user.new(config.get('user_email','user_name'),config.get('user_email','password'))

    #Email data
    email_to_send=email()
    email_to_send.new(user.get_user,"jcarolinares@gmail.com","La clase email funciona","En un lugar de la mancha")


    #Sending the email
    mime_message = MIMEText(email_to_send.get_message())
    mime_message["From"] = email_to_send.get_from_address()
    mime_message["To"] = email_to_send.get_to_address()
    mime_message["Subject"] = email_to_send.get_subject()
    smtp = SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(user.get_user(), user.get_password())
    smtp.sendmail(email_to_send.get_from_address(), email_to_send.get_to_address(), mime_message.as_string())
    smtp.quit()

if __name__ == "__main__":
 main()
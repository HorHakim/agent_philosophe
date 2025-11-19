from mail_sender import send_mail
from philosophic_agent import generate_philosophic_mail
import pandas
import time

def send_philosophic_mail(email):
    try:        
        philosophic_mail = generate_philosophic_mail()
        subject = philosophic_mail["sujet"]
        message = philosophic_mail["contenu"]
        send_mail(subject, message, email)

    except Exception as error:
        print("Le batch a échoué, nous allons retenter notre chance ;)")
        print(error)
        time.sleep(5)




if __name__ == '__main__':
    send_philosophic_mail(email="ticketsdata5@gmail.com")
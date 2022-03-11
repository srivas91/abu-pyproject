import smtplib
import schedule
import time


def sendtomail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('srini.pit21@gmail.com', 'srini_123')
    sender_address = 'srini.pit21@gmail.com'
    receiver_address = 'abu633855@gmail.com'
    text = 'good morning abu'
    server.sendmail(sender_address, receiver_address, text)
    server.quit()


schedule.every(5).seconds.do(sendtomail)

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
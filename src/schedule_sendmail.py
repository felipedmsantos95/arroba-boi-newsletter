import schedule
import time
import utils.send as send

schedule.every().saturday.at("08:00").do(send.email_ox)

#Antother schedule use examples:

#schedule.every(5).seconds.do(send.email_ox)
#schedule.every(1).minutes.do(send.email_ox)
#schedule.every().hour.do(send.email_ox)
#schedule.every().day.at("10:30").do(send.email_ox)
#schedule.every(5).to(10).minutes.do(send.email_ox)
#schedule.every().monday.do(send.email_ox)
#schedule.every().minute.at(":34").do(send.email_ox)
print('Schedule email will be sent every saturday..')
while True:
    schedule.run_pending()
    time.sleep(1)
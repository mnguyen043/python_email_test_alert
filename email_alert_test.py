import smtplib

content = 'TEST EMAIL'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('mrmikenguyen89@gmail.com','<SECRET_CODE>')

mail.sendmail('mrmikenguyen89@gmail.com','mrmikenguyen89@gmail.com',content)

mail.close()
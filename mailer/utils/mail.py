import smtplib
from email.mime.text import MIMEText

class Mail(object):
	def __init__(self, file_name, host='localhost'):
		self.messg = None
		if file_name:
			fp = open(file_name, 'rb')
			self.messg = MIMEText(fp.read())
			fp.close()
		self.sender = smtplib.SMTP(host)

	def send_mail(self, sender, recievers, subject, messg=None):
		if not messg:
			self.messg['Subject'] = subject
			self.messg['From'] = sender
			self.messg['To'] = recievers
		# do parsing in else
		self.sender.sendmail(sender, recievers, self.messg.as_string())
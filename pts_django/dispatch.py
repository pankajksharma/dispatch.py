import sys, os, re
from django.core.mail import send_mail

from models import Subscribers
from utils.message import Message
from utils.loggings import Logging

#Univeral Logging
log_file = "logs.txt"
log = Logging(log_file)

def get_package_name():
	"""Loads package name from command line arguments."""
	package = None
	try:
		if len(sys.argv) > 1:
			package = sys.argv[-1].lower()
	except Exception,e:
		print str(e)
		log.error(str(e))
	finally:
		return package

def get_keyword(package):
	"""Returns keyword (from supplied package name, if any)."""
	try:
		substr = re.search(r'(\S+)_(\S+)', package)
		if substr:
			return substr.group(2)
	except Exception,e:
		log.error(str(e))
		return None

def send_mails_to_all(message_client, receiver_emails=[]):
	receiver_emails.append('archive-outgoing@packages.qa.debian.org')
	log.info('Sending mails to ')
	message_client.add_headers()
	message = message_client.get_message()
	subject = message_client.get_header_component("subject") or "<Some subject>"
	sender = message_client.get_header_component("From") or "<Default Sender>"
	send_mail(subject, message, sender, receiver_emails, fail_silently=False)

def send_mails():
	content = sys.stdin.read()
	package_name = get_package_name()
	if not package_name:
		log.error('No package name suggested.')
		exit(1)
	keyword = get_keyword(package_name)
	message_cl = Message(content, package_name, keyword)
	message = message_cl.get_message()
	tag = message_cl.get_tag()
	message_cl.set_keyword(tag)
	log.info('(Tag, Keyword): (%s %s)' %(tag, keyword))
	subscribers = Subscribers.get_subscribers_email(package_name, tag) 
	# print package_name, keyword, message, tag, subscribers
	send_mails_to_all(message_cl, list(subscribers))
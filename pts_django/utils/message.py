import email
import re

class Message(object):
	def __init__(self, message, package_name, keyword):
		self.message = message
		self.package_name = package_name
		self.keyword = keyword
		self.messg = email.message_from_string(self.message)

	def get_message(self):
		return self.messg

	def set_keyword(self, new_keyword):
		self.keyword = new_keyword

	def get_header_component(self, header):
		return self.messg.get(header, "")
		
	def add_headers(self):
	    """Adds Revelant headers to the mail."""
	    self.messg.add_header('Precedence', 'list')
	    self.messg.add_header('X-Loop', '%s@packages.qa.debian.org' % self.package_name)
	    self.messg.add_header('X-Debian', 'PTS')
	    self.messg.add_header('X-Debian-Package', self.package_name)
	    self.messg.add_header('X-PTS-Package', self.package_name)
	    self.messg.add_header('X-PTS-Keyword', self.keyword)
	    self.messg.add_header('List-Unsubscribe', '<mailto:pts@qa.debian.org?body=unsubscribe%20' + self.package_name + '>')
	
	def get_header_info(self, header, reg_exp):
		"""Retrieves information from headers."""
		return re.match(reg_exp, self.messg.get(header, ""))

	def get_tag(self):
	    """Retuns tag for given message."""
	    tag = None
	    if not self.keyword:
	        tag = 'default'
	    elif self.get_header_info('X-Loop', r'owner@bugs\.debian\.org') and\
	            self.get_header_info('X-Debian-PR-Message', r'^transcript'):
	        tag = 'bts-control'
	    elif self.get_header_info('X-Loop', r'owner@bugs\.debian\.org') and\
	            self.messg.has_key('X-Debian-PR-Message'):
	        tag = 'bts'
	    elif self.get_header_info('Subject', r'^Accepted|INSTALLED|ACCEPTED') and\
	            re.match(r'\.dcs\s*$', self.messg.get_payload()) and self.messg.has_key('X-DAK'):
	        tag = 'upload-source'
	    elif self.messg.has_key('X-DAK') and self.get_header_info('Subject', r'^Accepted|INSTALLED|ACCEPTED'):
	        tag = 'upload-binary'
	    elif self.messg.has_key('X-DAK') or self.get_header_info('Subject', r'^Comments Regarding .*.changes$'):
	        tag = 'katie-other'
	    return tag
	 
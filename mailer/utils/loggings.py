import logging

class Logging(object):
	def __init__(self, file_name=None):
		if file_name:
			logging.basicConfig(filename=file_name,level=logging.DEBUG)
		logging.basicConfig(level=logging.DEBUG)
		logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

	def debug(self, messg):
		logging.debug(messg)

	def info(self, messg):
		logging.info(messg)

	def warning(self, messg):
		logging.warning(messg)

	def error(self, messg):
		logging.error(messg)
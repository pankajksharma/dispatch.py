from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db.utils import IntegrityError
from mailer.models import Tags

class Command(BaseCommand):
	help = 'Sends mail to relevent subscribers'

	def handle(self, *args, **kwargs):
		call_command('syncdb', interactive=False)
		try:
			for tag in Tags.VALID_TAGS:
				tag_ob = Tags(name=tag[0], description=tag[1])
				tag_ob.save()
				print 'Createing tag: %s' %tag_ob
		except IntegrityError:
			print "Some tags already exists."
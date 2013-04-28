from django.db import models
from django.utils import timezone

class Subscribers(models.Model):
	"""Base class for Subscribers."""
	email_id = models.EmailField(max_length=200)

	def __unicode__(self):
		return self.email_id

	@staticmethod
	def get_subscribers_email(package_name, tag):
		"""Returns list of emails of Interested Subscribers for given package name and tag."""
		subscribers = Subscribers.objects.values_list('email_id', flat=True)
		subscribers = subscribers.filter(subscriptions__package__name__exact=package_name, subscriptions__tag__name__exact=tag).all()	
		return subscribers

class Packages(models.Model):
	"""Base class for Packages."""
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Tags(models.Model):
	"""Base class for tags."""
	VALID_TAGS = (
		('bts', 'All Bugs'),
		('bts-control', 'Bug report status changes'),
		('upload-source', 'Notification from dak'),
		('katie-other', 'Warning and Error from dak'),
		('buildd', 'Build failures notifications'),
		('default', 'Any non-automatic email sent to the PTS'),
		('contact', 'Mails sent to the maintainer'),
		('summary', 'Regular summary emails about the package'),
		('upload-binary', 'When an uploaded binary package is accepted'),
		('cvs', 'VCS commit notifications'),
		('ddtp', 'Translations of descriptions or debconf templates'),
		('derivatives', 'Information about changes made to the package in derivative distributions'),
		('derivatives-bugs', 'Bugs reports and comments from derivative distributions')
	)

	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=250)

	def __unicode__(self):
		return '%s (%s)' %(self.name, self.description)

class Subscriptions(models.Model):
	"""Base class for Subscriptions. Has many to many relation with Subscribers and Packages"""
	subscriber = models.ManyToManyField(Subscribers)
	package = models.ManyToManyField(Packages)
	tag = models.ManyToManyField(Tags)
	created_on = models.DateTimeField(default=timezone.now())

	def __unicode__(self):
		return self.package
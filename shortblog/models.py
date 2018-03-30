from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user=models.OneToOneField(User)
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	avatar=models.FileField(null=True,blank=True)

	class Meta:
		db_table='UserProfile'
		ordering=['user_id']

	def get_url(self):
		return reverse('user-detail',args=[str(self.id)])

	def __str__(self):
		return self.user.username
	

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)


class Blog(models.Model):
	
	title=models.CharField(max_length=200)
	author=models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
	image=models.FileField(null=True,blank=True)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	draft=models.BooleanField(default=False)
	publish=models.DateField(auto_now=False,auto_now_add=False)
	content=models.TextField(null=True)
	
	class Meta:
		ordering = ["-timestamp"]
		db_table='Blog'

	def get_url(self):	
		return reverse('blog-detail',args=[str(self.id)])

	def __str__(self):
		return (self.title)

class BlogComment(models.Model):
	description=models.CharField(max_length=200)
	author=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
	blog=models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True)
	post_date=models.DateField(auto_now=False,auto_now_add=True)

	class Meta:
		ordering=["post_date"]

	def get_url(self):	
		return reverse('blog-detail',args=[str(self.id)])


	def __str__(self):
		return(self.description)


		
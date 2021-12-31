from django.db import models

# Create your models here.
class Add_project(models.Model):
	title = models.CharField('title',max_length=50,null=False)
	image = models.ImageField(null=False)
	description = models.TextField('description',null=False)
	Create_at = models.DateTimeField('Create_at',auto_now_add=True)
	url = models.CharField('url',max_length=50,null=False,default='')

	def __str__(self):
		return self.title
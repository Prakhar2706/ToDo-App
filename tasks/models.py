from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField(null=True, blank=True)
	priority = models.BooleanField(default=False)
	file_attachment = models.FileField(upload_to='task_files/', null=True, blank=True)

	def __str__(self):
		return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', default='static/profile/default.jpg', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
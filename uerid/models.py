from django.db import models
from django.contrib.auth.models import User

class REGISTER(models.Model):
	writer = models.ForeignKey(User)

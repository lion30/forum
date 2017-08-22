import os 
os.environ['DJANGO_SETTINGS_MODULE'] = 'forum.settings'

import django
django.setup()

from usercenter.models import UserProfile
from django.contrib.auth.models import User


for u in User.objects.all():
	p = UserProfile(user=u)
	p.save()




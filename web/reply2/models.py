
from django.db import models

from accounts.models import User2
from board.models import Post
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Reply(models.Model):
    contents = models.TextField()
    writer = models.ForeignKey(User2, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

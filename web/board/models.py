from django.db import models

# Create your models here.

from django.conf import settings

from accounts.models import User2

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title =models.CharField(max_length=100)
    contents = models.CharField(max_length=500)
    writer = models.ForeignKey(User2,on_delete=models.CASCADE) #이 유저 정보가 사라졌을때 나머지 정보(게시글을 어떻게 처리할 것이냐
    create_date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User2, related_name='likes',blank =True)

    def __str__(self):
        return ' 뿅 title = {},contents : {}'.format(self.title,self.contents)

class PostImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # null은 db에 값이 비어도 된다, blank는 프론트에서 값을 비워도 된다.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title =models.CharField(max_length=100)
    contents = models.CharField(max_length=500)
    def __str__(self):
        return ' 뿅 title = {},contents : {}'.format(self.title,self.contents)

class PostImage(models.Model):
    image = models.ImageField(upload_to='images/',null=True ,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    #null은 db에 값이 비어도 된다, blank는 프론트에서 값을 비워도 된다.
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from rest_framework.authtoken.admin import User

from product.models import Product


class Review(models.Model):
    contents = models.CharField(max_length=100)
    score = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
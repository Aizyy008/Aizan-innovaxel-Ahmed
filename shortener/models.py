import random
from django.db import models
import string

# Create your models here.
class URL(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    # @classmethod
    # def generate_short_code(cls, length=6):
    #     chars = string.ascii_letters + string.digits
    #     while True:
    #         short_code = ''.join(random.choice(chars) for _ in range(length))
    #         if not cls.objects.filter(short_code=short_code).exists():
    #             return short_code
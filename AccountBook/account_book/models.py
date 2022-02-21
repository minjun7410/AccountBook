from django.db import models
from django.utils import timezone


# Create your models here.
class AccountBook(models.Model):  # 트랜잭션을 저장하는 테이블
    email = models.ForeignKey('user.User', on_delete=models.CASCADE)  # on_delete=models.CASCADE : 이 외래키가 지정하는 행이 지워지면 현재 행도 지워짐
    price = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    description = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=50, default='')

    def define(self, email, price, year, month, day, description, location):
        self.email = email
        self.price = price
        self.year = year
        self.month = month
        self.day = day
        self.description = description
        self.location = location
        return



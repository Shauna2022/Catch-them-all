from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
PRICE = (
    ('H', 'High'),
    ('M', 'Mid'),
    ('L', 'Low')
)

class Cards(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    hp = models.IntegerField()
    move_name_1 = models.CharField(max_length=100)
    move_name_2 = models.CharField(max_length=100)
    weakness_type = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
  
    def __str__(self):
        return self.name
    def detail(self):
        return reverse('cards_detail', kwargs={'card_id': self.id})

class Selling(models.Model):
  date = models.DateField('Price range')
  price = models.IntegerField(
    max_length=1,
    choices=PRICE,
    default=PRICE[0][0]
    )
card = models.ForeignKey(Cards, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_price_display()} on {self.date}"
from django.db import models
from django.urls import reverse

# Create your models here.

class Cards(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    hp = models.IntegerField()
    move_name_1 = models.CharField(max_length=100)
    move_name_2 = models.CharField(max_length=100)
    weakness_type = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
   
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def detail(self):
        return reverse('cards_detail', kwargs={'card_id': self.id})
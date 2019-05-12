from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField()  # blank=True 지정하지 않은 경우
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_detail', kwargs={'pk': self.pk})


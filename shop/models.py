from django.db import models
from django.urls import reverse
from django.conf import settings
from pytz import timezone

class Item(models.Model):  # 과제추가
    name = models.CharField('상품명', max_length=20)
    desc = models.TextField(blank=True)
    photo = models.ImageField()
    price = models.CharField('가격', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.name
    
    def short_content(self):
        if self.desc:
            d = self.desc[:20] + '...'
        else:
            d = '(내용 없음)'
        return d
    short_content.short_description = '간략 설명'
    
    def get_absolute_url(self):  # 과제 추가
        return reverse('shop:item_detail', kwargs={'pk':self.pk})
    

def local_time(input_time):  # 과제추가
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)

class Review(models.Model):  # 과제추가
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                                related_name='reviews', verbose_name='리뷰')
    review_cmt = models.TextField('리뷰글')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-item__id', '-id']
        
    def __str__(self):
        return self.review_cmt
    
    def updated(self):
        return local_time(self.updated_at)
    
    updated.short_description = '수정 일시'
        
        


from django.contrib import admin
from .models import Item, Review

# admin.site.register(Item)

# 과제추가
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_content', 'photo', 'created_at', 'updated_at']
    list_display_links = ['id', 'name',]
    list_filter = ['created_at', 'updated_at',]
    search_fields = ['name', 'desc',]
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'review_cmt', 'updated_at',]
    list_display_links = ['id', 'review_cmt',]

    
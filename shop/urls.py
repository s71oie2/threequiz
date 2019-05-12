from django.urls import path, register_converter
from shop import views
from shop import converters

app_name = 'shop'

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.item_list, name='item_list'),                        # 조회
    path('view/<int:pk>/', views.item_detail, name='item_detail'),      # 조회
    path('new/', views.item_new, name='item_new'),                      # 등록
    path('remove/<int:pk>/', views.item_remove, name='item_remove'),    # 삭제
    path('edit/<int:pk>/', views.item_edit, name='item_edit'),          # 수정
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings                         # 추가 1
from django.conf.urls.static import static
from prj.views import HomeView, UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('', HomeView.as_view(), name='home'),
    path('shop/', include('shop.urls'), name='shop'),
    path('blog/', include('blog.urls'), name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:                                       # 추가 2
    import debug_toolbar                                 # 추가 2
    urlpatterns += [                                     # 추가 2
        path('__debug__/', include(debug_toolbar.urls)), # 추가 2
    ]                                                    # 추가 2

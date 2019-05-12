from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from blog.models import *
from shop.models import *



class FirstMixin(TemplateView):
    model = Post
    def get_context_data(self, **kwargs):
        pst = super(FirstMixin, self).get_context_data(**kwargs)
        pst['posts'] = Post.objects.all().order_by('-updated_at')[:3]
        return pst
    
class SecondMixin(TemplateView):
    model = Item
    def get_context_data(self, **kwargs):
        ctx = super(SecondMixin, self).get_context_data(**kwargs)
        ctx['items'] = Item.objects.all().order_by('-price')[:3]
        return ctx
    
    
class HomeView(FirstMixin, SecondMixin):
    # model = Post, Item
    template_name = 'home.html'
    
    
    
    
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

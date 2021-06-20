from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'beer'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('review_create', views.ReviewCreateView.as_view(), name="review_create"),
  path('beer_detail/<int:pk>/', views.DetailView.as_view(), name="beer_detail"),
  path('new/', TemplateView.as_view(template_name='new_index.html'), name='new'),
  path('get/', views.get_beer, name='get_beer'),
]
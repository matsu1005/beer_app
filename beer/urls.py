from django.urls import path

from . import views

app_name = 'beer'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('review_create', views.ReviewCreateView.as_view(), name="review_create")
]
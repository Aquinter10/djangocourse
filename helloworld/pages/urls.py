from django.urls import path 
from .views import HomePageView, ContactPageView, AboutPageView, ProductIndexView, ProductShowView

 
urlpatterns = [ 
path("", HomePageView.as_view(), name='home'),
     path("contact/", ContactPageView.as_view(), name='contact'),
     path('about/', AboutPageView.as_view(), name='about'),
     path('products/', ProductIndexView.as_view(), name='index'), 
     path('products/<str:id>', ProductShowView.as_view(), name='show'),
  ]
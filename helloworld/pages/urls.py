from django.urls import path 
from .views import HomePageView, ContactPageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreated 

 
urlpatterns = [ 
path("", HomePageView.as_view(), name='home'),
     path("contact/", ContactPageView.as_view(), name='contact'),
     path('about/', AboutPageView.as_view(), name='about'),
     path('products/', ProductIndexView.as_view(), name='index'),
     path('products/productcreated', ProductCreated.as_view(), name='create'),  
     path('products/create', ProductCreateView.as_view(), name='form'), 
     path('products/<str:id>', ProductShowView.as_view(), name='show'),
     
     
  ]
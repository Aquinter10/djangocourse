from django.shortcuts import render
from django.views.generic import TemplateView  
from django.views import View 
from django.http import HttpResponseRedirect
from django.urls import reverse
class HomePageView(TemplateView):
     template_name = 'pages/home.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Your Name", 
        }) 
 
        return context 
    
 
class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV","price": 1000}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone","price": 2000}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast","price": 1500}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses","price": 5000} 
    ] 
 
class ProductIndexView(View): 
    template_name = 'products/index.html' 
 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
 
        return render(request, self.template_name, viewData) 
 
class ProductShowView(View): 
    template_name = 'products/show.html' 
 
    def get(self, request, id): 
        try:
            product_index = int(id) - 1
            if product_index < 0 or product_index >= len(Product.products):
                raise IndexError
            product = Product.products[product_index]
        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse('home'))

        viewData = {
            "title": product["name"] + " - Online Store",
            "subtitle": product["name"] + " - Product information",
            "product": product,
            "price": str(product["price"]) + " $ USD"
        }

        return render(request, self.template_name, viewData)

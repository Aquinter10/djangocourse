from django.shortcuts import render, redirect
from django.views.generic import TemplateView  
from django.views import View 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class HomePageView(TemplateView):
     template_name = 'pages/home.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

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
    
class ProductCreated(TemplateView): 
    template_name = 'products/productcreated.html'
    
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
    
class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 
 
 
class ProductCreateView(View): 
    template_name = 'products/create.html' 

    def get(self, request): 
        form = ProductForm() 
        viewData = {
            "title": "Create product",
            "form": form
        }
        return render(request, self.template_name, viewData) 

    def post(self, request): 
     form = ProductForm(request.POST) 
     if form.is_valid(): 
        price = form.cleaned_data.get("price")
        if price is not None and price <= 0:
            form.add_error("price", "The price must be greater than zero.")
        else:
            return redirect('create')  # Redirige a la vista

     viewData = {
        "title": "Create product",
        "form": form
          }
     return render(request, self.template_name, viewData)




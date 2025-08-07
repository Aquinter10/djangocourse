from django.shortcuts import render, redirect,  get_object_or_404
from django.views.generic import TemplateView , ListView 
from django.views import View 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Product 

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
    

class ProductIndexView(View): 
    template_name = 'products/index.html' 
 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.objects.all()  
 
        return render(request, self.template_name, viewData) 
 
class ProductShowView(View): 
    template_name = 'products/show.html' 

    def get(self, request, id): 
        try:
            product = get_object_or_404(Product, pk=id)
        except ValueError:
            return HttpResponseRedirect(reverse('home'))

        viewData = {} 
        viewData["title"] = product.name + " - Online Store" 
        viewData["subtitle"] =  product.name + " - Product information" 
        viewData["product"] = product 

        return render(request, self.template_name, viewData)

    
class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product 
        fields = ['name', 'price'] 
 
 
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
        form.save()  
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

class ProductListView(ListView): 
    model = Product 
    template_name = 'product_list.html' 
    context_object_name = 'products'  # This will allow you to loop through 'products' in your template 
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Products - Online Store' 
        context['subtitle'] = 'List of products' 
        return context 


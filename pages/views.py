from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Contacto
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView



''''class HomePageView(TemplateView):
    template_name = 'home.html' '''    
def home(request):
    if request.method == 'POST':
        form = Contacto(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/#contacto')
        else:
            form = Contacto()
            return render (request,'home.html',{'form':form})
    if request.method == "GET":
        form = Contacto()
        return render (request,'home.html',{'form':form})







"""
 def ContactoForm(request):
    if request.method == 'POST':
        form =  Contacto(request.POST)
        if form.is_valid():
            _nombre = form.cleaned_data['nombre'] 

"""


                


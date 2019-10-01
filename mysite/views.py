from django.views.generic import (ListView, DetailView, CreateView,TemplateView)
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import House
from .forms import HouseCreateForm
from django.http import HttpResponse


class HouseListView(ListView):
    model = House
    template_name = "index.html"
    context_object_name = "propert"
    ordering = ['-id']


class HouseDetailView(LoginRequiredMixin,DetailView):
    model = House
    template_name = "property-single.html"


def createHouse(request):
    form = HouseCreateForm(request.POST)
    if form.is_valid():
        post = form.save()
        return redirect('index')
    else:
        form = HouseCreateForm()

    return render(request, 'test_house_form.html', {'form': form})





class AboutView(TemplateView):
    template_name = 'about.html'


class PropertyGrid(LoginRequiredMixin,ListView):
    model = House
    template_name = "property-grid.html"
    context_object_name = "propert"
    ordering = ['-id']



@login_required()
def blog_grid(request):
    return render(request, 'blog-grid.html')

class ContactView(TemplateView):
    template_name = 'contact.html'


def agent_single(request):
    return render(request, 'agent-single.html')
def agents_grid(request):
    return render(request, 'agents-grid.html')



def blog_single(request):
    return render(request, 'blog-single.html')





###################      EXTRA ###########################


# Create your views here.

# def index(request):
#     context = {
#         'propert': House.objects.all()}
#     return render(request, 'index.html', context)


# @login_required()
# def property_single(request,prop_id):
#
#     context = {
#         'property' : House.objects.get(pk = prop_id)}
#     return render(request,'property-single.html',context)




# def contact(request):
#     return render(request, 'contact.html')


# def property_grid(request):
#
#     return render(request, 'property-grid.html', {'propert' : propert})


# def property_grid(request):
#     for i in House.objects:
#         list.append(i)
#     args = {'posts': propert}
#     return render(request,'property-grid.html', args)


# @login_required()
# def property_grid(request):
# 	context ={
# 	'propert': House.objects.order_by('-id')}
# 	return render(request,'property-grid.html',context)

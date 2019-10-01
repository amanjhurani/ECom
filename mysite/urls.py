from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import (HouseListView,
                    ContactView,
                    AboutView,
                    PropertyGrid,
                    HouseDetailView,)
from django.urls import path
from . import views

urlpatterns = [
    path('', HouseListView.as_view(), name='index'),
    #path('index.html', views.index, name='index-home'),
    path('about/',AboutView.as_view(), name = 'about'),
    path('property-grid/', PropertyGrid.as_view(), name='property_grid'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog-grid.html', views.blog_grid, name='blog_grid'),
    path('agent-single.html', views.agent_single, name='agent_single'),
    path('agents-grid.html', views.agents_grid, name='agents_grid'),
    path('property-single/<int:pk>/',HouseDetailView.as_view(), name='property_single'),
    path('property-upload/new/',views.createHouse , name='property_upload'),
    path('blog-single.html', views.blog_single, name='blog_single')

]

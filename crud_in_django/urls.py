from django.contrib import admin
from django.urls import path
from clients import views 
urlpatterns = [
    path('', views.clnt, name='main-view'),
    path('admin/', admin.site.urls),
    path('clnt', views.clnt),  
    path('error', views.error), 
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]

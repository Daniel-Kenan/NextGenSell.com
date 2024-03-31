from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'consultancy'

urlpatterns = [
    path('', views.dashboard, name="cs_dashboard"),
    path('potential_clients/', views.potential_clients, name="cs_potential_clients"),
    path('existing_clients/',views.existing_clients , name="cs_existing_clients"),
    path('product_keys/', views.productkeys, name="cs_product_keys"),
    path('notifications/', views.notifications, name="cs_notifications"),
    path('profile/', views.profile, name="cs_profile"),
    path('bussiness/', views.bussiness_form, name="cs_Bform"),  
     path('add-client/', views.add_client, name='add_client'), 
]
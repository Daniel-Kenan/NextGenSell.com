from django.urls import path
from .views import dashboard,profile,existing_clients,potential_clients,productkeys,notifications,bussiness_form
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', dashboard, name="cs_dashboard"),
    path('potential_clients/', potential_clients, name="cs_potential_clients"),
    path('existing_clients/',existing_clients , name="cs_existing_clients"),
    path('product_keys/', productkeys, name="cs_product_keys"),
    path('notifications/', notifications, name="cs_notifications"),
    path('profile/', profile, name="cs_profile"),
    path('bussiness/', bussiness_form, name="cs_Bform"),   
]
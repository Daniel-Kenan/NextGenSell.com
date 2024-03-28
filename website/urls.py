from django.urls import path
from .views import home, clientsignin
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', home, name="home"),
    # path('validate-product-key-docs/<str:key>/<str:device>',validate_product_key_view, name='validate_product_key_docs'),
    # path('validate-product-key-api/<str:key>/<str:device>',ValidateProductKeyView.as_view(), name='validate_product_key_func'), 
    path('signin',clientsignin, name="clientsignin")
]
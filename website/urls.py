from django.urls import path
from . import views 
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name="home"),
    # path('validate-product-key-docs/<str:key>/<str:device>',validate_product_key_view, name='validate_product_key_docs'),
    # path('validate-product-key-api/<str:key>/<str:device>',ValidateProductKeyView.as_view(), name='validate_product_key_func'), 
    path('signin/',views.clientsignin, name="clientsignin"),
    path('login/', views.login_view, name='login_view'),
    path('5ftr4vt6bv4e/',views.testpage,name="testpage"),
    path('payment-successful/' , views.payment_success, name='payment_successful'),
     path('payment-failed/' , views.payment_failure, name='payment_failed'),
     path('payment-cancelled/' , views.payment_cancelled, name='payment_cancelled'),
     path('contact-us-form/', views.ContactUsHandling.as_view(), name='contact-us-form'),
     path('signout/', views.sign_out, name='sign-out'),
    path('signup/', views.sign_up, name='sign-up'),
    path('submit-client/', views.submit_form, name='submit_form')
    # path('signup/', RedirectView.as_view(pattern_name='contact-us-form'), name='sign-up'),
]

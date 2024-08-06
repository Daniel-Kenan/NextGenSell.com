from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "retailoffice"

urlpatterns = [
  path('backedup-data/', views.my_view, name='my_view'),
  path('', views.office_dashboard, name="office_dashboard"),
  path('chatbot', views.chatbot, name="office_chatbot"),
  path('calculator', views.calculator, name="office_calculator"),
  path('advancedreports', views.advanced_reports, name="journals"),
  path('products', views.retrieve_products, name="products"),
]
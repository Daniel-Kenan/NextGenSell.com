"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

def user_is_admin(user):
    return user.is_authenticated and user.is_staff

urlpatterns = [
    #    path('admin/defender/', include('defender.urls')),
    path('api_schema/', user_passes_test(user_is_admin)(
        get_schema_view(
            title='API Schema',
            description='Guide for the REST API'
        )
    ), name='api_schema'),

    path('docs/', user_passes_test(user_is_admin)(
        TemplateView.as_view(
            template_name='docs.html',
            extra_context={'schema_url': 'api_schema'}
        )
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path("",include("website.urls")),
    path("cs/",include("consultant.urls")),
    path("RetailBackOffice/",include("RetailBackOffice.urls"))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
else: urlpatterns += [ re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]
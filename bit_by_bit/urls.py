"""bit_by_bit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# From views.py file import the index name
# Dot symbol forces to lookup in the current directory
from .views import index

# Import values from settings.py file
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Add empty url processing, forcing to call the index function
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
# Point Django to the directories where static files to search for
# Take the values from settings.py file
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

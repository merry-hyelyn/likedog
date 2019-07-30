"""like_dog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import dog.views
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dog.views.info, name='info'),
    path('home/', dog.views.home, name='home'),
    path('print/', dog.views.make_print, name='print'),
    path('enroll/',dog.views.enroll,name="enroll"),
    path('print_new/',dog.views.print_new,name="print_new"),
    path('enroll_page/',dog.views.enroll_page, name = "enroll_page"),
    path('delete/<int:id>', dog.views.delete, name= "delete"),
    path('content/<int:id>', dog.views.content, name = "content"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

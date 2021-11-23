"""ashaworker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ashaworkapp import admin_urls, doctor_urls, patient_urls, ashaworker_urls
from ashaworkapp.views import Index_View, Patient_Reg, Doctor_Reg, Ashaworker_Reg, LoginView, Services, \
    Forgotpassword
from ashaworker import settings

urlpatterns = [
    path('', Index_View.as_view()),
    path('patient_reg', Patient_Reg.as_view()),
    path('doctor_reg', Doctor_Reg.as_view()),
    path('ashaworker_reg', Ashaworker_Reg.as_view()),
    path('login', LoginView.as_view()),
    path('services', Services.as_view()),
    path('forgot', Forgotpassword.as_view()),
    # path('admin/', admin.site.urls),
    path('doctor/', doctor_urls.urls()),
    path('patient/', patient_urls.urls()),
    path('ashaworker/', ashaworker_urls.urls()),
    path('admin/', admin_urls.urls()),
    # path('accounts/', include('django.contrib.auth.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



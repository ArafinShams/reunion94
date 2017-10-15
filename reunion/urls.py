"""reunion URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
#User Login View
from django.contrib.auth.views import LoginView,logout

from registrations.views import (
    RegistredListview, #ClassBases LIST view
    RegistredDetailView,#ClassBases DETAIL view
    Registration_createview,#ClassBases DETAIL view
    PaymentUpdate
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

# Static Pages
    url(r'^$', TemplateView.as_view(template_name='static_home.html'), name='home'),
	url(r'^program/$', TemplateView.as_view(template_name ='static_program.html'), name='program'),
	url(r'^contact/$', TemplateView.as_view(template_name ='static_contact.html'), name='contact' ),

#Login View
    url(r'^login/$', LoginView.as_view(), {'next': 'home'}, name='login'),

#Logout URL
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),

# Registered List
    #Using Functionbased View
    #url(r'^registredlist/', Registred_Listview), #FunctionBasedview 
    url(r'^registration/$', RegistredListview.as_view(), name='resistredlist'), #ClassBased view

# Registered Details
    # # Details using Primary Key
    url(r'^registration/(?P<pk>[0-9]+)/$', RegistredDetailView.as_view(), name='registred_details'),

# Registrations Create View
    url(r'^registration/create/$', Registration_createview, name='registration'),

#Update Payment
   url(r'^registration/(?P<pk>[0-9]+)/payment/$', PaymentUpdate.as_view(), name='payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
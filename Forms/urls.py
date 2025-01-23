"""
URL configuration for Forms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import RedirectView

from myapp.views import contact_view
from myapp.views import contact_list_view
from myapp.views import contact_edit_view
from myapp.views import login_view





urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('', RedirectView.as_view(url='/login/')),  # Redirect root to /contact/
    path('contact/list/', contact_list_view, name='contact_list'),  # List URL
    path('contact/edit/<int:pk>/', contact_edit_view, name='contact_edit'),
    path('login/', login_view, name="login"),


]

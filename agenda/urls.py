"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/<event_title>/', views.show_local),
    path('json/events/list', views.json_list),
    path('eventos-list/', views.list_events),
    path('past/events/', views.past_events),
    path('eventos-list/new/', views.new_event),
    path('eventos-list/new/submit', views.submit_event),
    path('eventos-list/delete/<int:evento_id>/', views.delete_event),
    path('', RedirectView.as_view(url='/eventos-list/')), # esta é outra maneira de fazer o redirecionamento
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]

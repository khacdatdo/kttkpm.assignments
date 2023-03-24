"""user_service URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from user_model.views import registration_req as reg_obj
from user_login.views import user_login as login_obj
from user_info.views import user_info as info_obj

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('userregistration/', reg_obj),
    url('userlogin/', login_obj),
    url('userinfo/', info_obj),
]

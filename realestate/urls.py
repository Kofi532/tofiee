"""
URL configuration for realestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from tofiee import views as tf
from django.conf import settings
from django.conf.urls.static import static
from tofiee.views import Memberview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", tf.first, name="home"),
    path("sell/", tf.sell, name="sell"),
    path("buy/", tf.buy, name="buy"),
    path("rent/", tf.rent, name="rent"),
    path("user/", tf.user, name="user"),
    path("boss/", tf.boss, name="boss"),
    path("register/", tf.register_request, name="register"),
    path("userinput/", tf.user_form, name="userinput"),
    path("p/", Memberview.as_view(), name='approve'),
    path('', include('tofiee.urls')),
    path('delete/<int:record_id>/', tf.delete_record, name='delete_record'),
    path('approve/<int:record_id>/', tf.approve_record, name='approve_record'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


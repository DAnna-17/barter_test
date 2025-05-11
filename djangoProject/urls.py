"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from barter import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)



urlpatterns = [
    path('data/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path("", views.lk_page, name='lk_page'),
    path("all/", views.ads_page, name='ads_page'),
    path('delete/<int:ad_id>', views.delete_ad, name='delete_ad'),
    path('edit/<int:ad_id>', views.edit_ad, name='edit_ad'),
    path("offers/", views.offers_page, name='offers_page'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("deny/<int:off_id>", views.deny_off, name="deny"),
    path("accept/<int:off_id>", views.accept_off, name="accept")
]
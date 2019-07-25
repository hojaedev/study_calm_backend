from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls import url
from accounts.api.urls import urlpatterns_auth
from accounts.api.urls import urlpatterns_accounts
from listings.api.urls import listing_urlpatterns
def login(request):
    return render(request, 'login.html')

urlpatterns = [
    path('login/', login),

    # AUTH
    path('auth/', include(urlpatterns_auth)),
    # LOCAL APPS
    path('api/accounts/', include(urlpatterns_accounts)),
    path('api/listings/', include(listing_urlpatterns)),

    path('', include('social_django.urls', namespace='social')),

    # ADMIN SITE
    path('admin/', admin.site.urls),


]

from social_django import urls
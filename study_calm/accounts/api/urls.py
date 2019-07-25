from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import accounts.api.views as view

from django.shortcuts import render


urlpatterns_auth = [
    # path('register/', view.register),
    # path('get_token/', view.get_token),
    # path('refresh_token/', view.refresh_token),
    # path('revoke_token/', view.revoke_token),
    # path('callback/', view.callback),
    path('callback/', view.callback),
    path('token/', view.token)
]

urlpatterns_accounts = [
    path('users/', view.UserList.as_view()),
    path('users/customers/<int:id>/', view.CustomerView.as_view()),
    path('users/suppliers/<int:id>/', view.SupplierView.as_view()),
]


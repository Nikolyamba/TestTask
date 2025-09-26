from django.contrib import admin

from django.urls import path

from payments.views import payments_chart

urlpatterns = [
    path("", payments_chart, name="payments_chart"),
]

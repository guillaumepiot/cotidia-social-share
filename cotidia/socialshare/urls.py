from django.urls import path

from cotidia.socialshare import views

app_name = 'cotidia.socialshare'

urlpatterns = [
    path('send-email', views.ShareEmail.as_view(), name='send-email'),
]


# from django.contrib import admin
from django.urls import path
from data_api.views import AudioUploadView

urlpatterns = [
    path('list/', AudioUploadView.as_view( )),
]

# myproject/urls.py или driveapi/urls.py

from django.urls import path
from api.views import CreateGoogleDocView

urlpatterns = [
    path('create-document/', CreateGoogleDocView.as_view(), name='create-document'),
]

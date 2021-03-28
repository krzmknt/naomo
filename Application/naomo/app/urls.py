from django.urls import path

from app.views.login import view as login_view
from app.views.index import view as index_view

urlpatterns = [
    path('login', login_view.top, name="login_top"),
    path('', index_view.top, name="index_top"),
]

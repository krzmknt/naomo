from django.urls import path

from app.views.login import view as login_view

urlpatterns = [
    path("", login_view.top, name="login_top")
]

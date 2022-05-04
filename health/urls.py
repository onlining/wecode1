from django.urls import path
from health.views import ping
urlpatterns = [
    path('pong/', ping)

]

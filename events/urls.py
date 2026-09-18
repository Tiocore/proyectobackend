from django.urls import path
from . import views


urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("<int:event_id>/", views.event_detail, name="event_detail"),
    path("<int:event_id>/results/", views.event_results, name="event_results"),
]

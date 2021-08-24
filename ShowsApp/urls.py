from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:id>', views.show_id),
    path('shows/<int:id>/edit', views.show_edit),
    path('shows/<int:id>/update', views.show_update),
    path('shows/<int:id>/destroy', views.show_destroy),
]

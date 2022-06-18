from django.urls import path

from blog import views


urlpatterns = [
    path('', views.list),
    path('create/new/', views.create_view),
    path('<str:slug>/detail/', views.detail),
    path('<str:slug>/edit/', views.update_view),
    path('<str:slug>/delete/', views.delete_view),

    
]

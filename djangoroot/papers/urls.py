from django.urls import path

from . import views

app_name = "papers"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:document_id>/", views.detail, name="detail"),
    path('upload/', views.upload_file, name='upload_file'),

]

from django.urls import path

from main_app.models import Widget
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widget/add', views.add_widget, name='add_widget'),
    path('widget/<int:pk>/delete/', views.WidgetDelete.as_view(), name='widget_delete'),
    
]

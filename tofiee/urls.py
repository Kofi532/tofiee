from . import views
from django.urls import path

urlpatterns = [
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('update/<int:id>', views.update, name='update'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('details/<slug:slug>/', views.UserDetail.as_view(), name='user_detail'),
]
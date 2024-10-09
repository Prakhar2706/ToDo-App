from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetForm

urlpatterns = [
	path('', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('complete/<str:pk>/', views.completeTask, name="complete_task"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='tasks/forgot_password.html'), name='forgot_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='tasks/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetForm.as_view(template_name='tasks/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='tasks/password_reset_complete.html'), name='password_reset_complete'),
]
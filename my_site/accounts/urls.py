from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	# HOME URL
	path('', views.home, name="home"),

	# MAIN AUTH URLS
	path('login/', views.account_login, name='account_login'),
	path('logout/', views.account_logout, name="account_logout"),
	path('signup/', views.account_signup, name="account_signup"),

	# PASSWORD RESET URL
	path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),
]
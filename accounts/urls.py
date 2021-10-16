from django.urls import path

from .views import RegisterView, LoginView, LogoutView, ForgotPasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register_user"),
    path('login/', LoginView.as_view(), name="login_user"),
    path('logout/', LogoutView.as_view(), name="logout_user"),
    path('forgot_password/', ForgotPasswordView.as_view(), name="forgot_password"),
]

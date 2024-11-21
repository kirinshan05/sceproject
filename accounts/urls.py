from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


app_name = 'accounts'

urlpatterns = [
    path('signup/',
        views.SignUpView.as_view(),
        name='signup'
        ),
    path('signup_success/',
        views.SignUpSuccessView.as_view(),
        name='signup_success'
        ),
    path('login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
        ),
    path('logout/',
        auth_views.LogoutView.as_view(template_name='logout.html'),
        name='logout'
        ),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name = "password_reset_sent.html"),
        name = 'password_reset_done'
        ),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name = "password_reset_sent.html"),
        name = 'password_reset_done'
        ),
    path('reset/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(
            template_name = "password_reset_form.html"),
        name ='password_reset_confirm'
        ),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name = "password_reset_done.html"),
        name = 'password_reset_complete'
        ),
]


# カスタムビューを作成する場合
# class CustomLoginView(LoginView):
#     template_name = 'login.html'

# urlpatterns = [
#     path('login/', CustomLoginView.as_view(), name='login'),
# ]

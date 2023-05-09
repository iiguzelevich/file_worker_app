from django.urls import path

from . import views

urlpatterns = [
    path('profile/<int:user_id>', views.view_personal_data, name='profile'),
    path(
        'profile/edit/<int:user_id>',
        views.edit_personal_data,
        name='edit_personal_data'
    ),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('about/', views.home, name='about'),
    path('services/', views.home, name='services'),
    path('news/', views.home, name='news'),
    path('contact/', views.home, name='contact'),

    path('load_txt/', views.load_txt, name='load_txt'),
    path('load_pdf/', views.load_pdf, name='load_pdf'),
    path('load_video/', views.load_video, name='load_video'),

    path('my_files/', views.my_files, name='my_files'),
    path('my_pdf_files/', views.my_pdf_files, name='my_pdf_files'),
    path('my_audio_files/', views.my_audio_files, name='my_audio_files'),
    path('my_gif_files/', views.my_gif_files, name='my_gif_files'),

    path(
        'edit_pdf/<str:file_name>/', views.edit_file_pdf, name='edit_file_pdf'
    ),
    path(
        'delete_pdf/<str:file_name>/', views.delete_file_pdf,
        name='delete_file_pdf'
    ),

    path(
        'edit_audio/<str:file_name>/', views.edit_file_audio,
        name='edit_file_audio'
    ),

    path(
        'delete_audio/<str:file_name>/', views.delete_file_audio,
        name='delete_file_audio'
    ),

    path(
        'edit_gif/<str:file_name>/', views.edit_file_gif,
        name='edit_file_gif'
    ),
    path(
        'delete_audio/<str:file_name>', views.delete_file_gif,
        name='delete_file_gif'
    ),
]

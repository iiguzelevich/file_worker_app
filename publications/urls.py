from django.urls import path

from . import views

urlpatterns = [
    path('publish/', views.publish, name='publish'),

    path(
        'publish_pdf/<str:file_name>', views.publish_pdf,
        name='publish_pdf'
    ),
    path(
        'publish_audio/<str:file_name>', views.publish_audio,
        name='publish_audio'
    ),
    path(
        'publish_gif/<str:file_name>', views.publish_gif,
        name='publish_gif'
    ),
    path(
        'publish/comment/<str:file_name>', views.comment_file,
        name='comment_file'
    ),
    path('subscribe/<str:file_name>', views.subscribe, name='subscribe'),

]

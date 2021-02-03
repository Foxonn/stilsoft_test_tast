from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path(
        '',
        views.ListPostsAPIView.as_view(),
        name='list_posts'
    ),
    path(
        '<int:pk>/',
        views.PostAPIView.as_view(),
        name='post'
    ),
]

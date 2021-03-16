from django.urls import path
from .views import (post_comment_create_and_list_view,
    like_unlike_post,
    PostDeleteView,
    PostUpdateView,
    MyPostsView,
    )

app_name = 'posts'

urlpatterns = [
    path('', post_comment_create_and_list_view, name='main-post-view'),
    path('liked/', like_unlike_post, name='like-post-view'),
    path('<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('my-posts/', MyPostsView.as_view(), name='my-posts-view'),
]
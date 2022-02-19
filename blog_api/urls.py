from django.urls import path
from .views import PostDetail, PostList, CreatePostWithImage, updatePost

urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(), name='detail' ),
    path('update/<int:id>/',updatePost.as_view(), name='updatePost' ),
    path('',PostList.as_view(), name='list' ),
    path('create/',CreatePostWithImage.as_view(), name='create post' )
]
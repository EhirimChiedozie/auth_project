from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')



urlpatterns = [
    path('create-post/', views.CreatePostView.as_view(), name='create-post'),
    # path('posts/', views.PostListView.as_view(), name='posts'),
    # path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('update-blogpost/<int:pk>/', views.UpdateBlogPost.as_view(), name='update-blogpost'),
    path('delete-blogpost/', views.DeleteBlogPost.as_view(), name='delete-blogpost'),
    path('posts/<int:post_id>/comments/', views.CommentList.as_view(), name='post-comments'),
]

urlpatterns += router.urls
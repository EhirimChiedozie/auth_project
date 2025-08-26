from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/social/', include('allauth.socialaccount.urls')),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create_todo/', views.CreateTodo.as_view(), name='create_todo'),
    path('view_todo/', views.TodoList.as_view(), name='view_todo'),
    path('view_todo/<int:pk>/', views.GetTodoByID.as_view(), name='todo_detail'),
    path('update_todo/<int:pk>/', views.UpdateTodo.as_view(), name='update_todo'),
    path('delete_todo/<int:pk>/', views.DeleteTodo.as_view(), name='delete_todo'),
    #path('todo_dates/', views.todo_dates, name='todo_date'),
]
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('user/delete/', views.DeleteUserView.as_view(), name='user-delete'),
    path('user/update/', views.UserUpdateView.as_view(), name='user-update'),
    # path('user/profile/', views.UserProfileView)
    path('detail/', views.account_detail, name='account_detail'),
    path('update/', views.account_update, name='account_update'),
    # path('likes/', views.likes, name='likes'),
]

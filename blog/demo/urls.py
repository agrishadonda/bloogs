from django.urls import path
from . import views
# from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView
urlpatterns = [
    path('',views.PostListView.as_view(),name='blogs'),
    path('detail/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('create/',views.PostCreateView.as_view(),name='create'),
    path('user/<str:username>',views.UserPostListView.as_view(),name='userlist'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete'),
    path('about/',views.about,name = 'abouts'),
]

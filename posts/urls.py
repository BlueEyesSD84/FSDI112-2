from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, AboutPageView, HomePageView

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>)/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(),name='home'),
] 
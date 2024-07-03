from django.urls import path
from pages.views import HomePageView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
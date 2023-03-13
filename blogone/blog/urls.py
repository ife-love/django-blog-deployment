from django.urls import path
from . import views

urlpatterns = [

    # path('home/', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('create_post/', views.CreatePostView.as_view(), name='create-post'),
    path('article/edit/<int:pk>/', views.UpdatePostView.as_view(), name='edit-post'),
    path('article/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post'),
    path('article/drafts/', views.DraftListView.as_view(), name='post-draft-list'),
    path('article/<int:pk>/publish/', views.post_publish, name='article-publish'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    ]
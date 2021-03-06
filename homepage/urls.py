from django.urls import path, include
from . import views
from .views import PostDetailView, CommentCreateView, public_profile, CommentUpdateView, CommentDeleteView, FollowerListView, PostDeleteView, PostUpdateView, likePost, SearchListView, PostListView, ExploreListView
# import notifications.urls

urlpatterns = [
    path('home/', PostListView.as_view(), name='gichurugram-home'),
    path('about/us/', views.aboutUs, name='gichurugram-about-us'),
    path('about/jobs/', views.aboutJobs, name='gichurugram-about-jobs'),
    path('about/', views.redirectAboutView, name='gichurugram-about-us-redirect'),
    path('', ExploreListView.as_view(), name='gichurugram-explore'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name='comment_form'),
    path('profile/<str:username>/', views.public_profile, name='public_profile'),
    path('post/new/', views.post, name='post-add'),
    path('post/<int:pk/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('profile/<str:username>/followers/', views.
         FollowerListView.as_view(), name='follower_list'),
    path('profile/<str:username>/following/', views.
         FollowerListView.as_view(), name='following-list'),
    path('post/<int:pk>/likes/', views.LikeListView.as_view(), name='likes-list'),
    path('search/', views.SearchListView.as_view(), name="search-list"),
    path('likepost/', views.likePost, name='likepost'),
    # path('inbox/notifications/', include(notifications.urls, namespace='notifications')),

]
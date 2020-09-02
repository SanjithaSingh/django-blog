from django.conf.urls import url
from blog import views


urlpatterns = [
    url('about', views.AboutView.as_view(), name="about"),
    url('post/<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
    url('post/new/', views.CreatePostView.as_view(), name="create_post"),
    url('post/<int:pk>/edit/', views.UpdatePostView.as_view(), name="edit_post"),
    url('post/<int:pk>/delete/', views.DeletePostView.as_view(), name="delete_post"),
    url('post/<int:pk>/publish/', views.publish_post, name="publish_post"),
    url('post/<int:pk>/comment', views.add_comment_to_post, name="add_comment_to_post"),
    url('drafts/', views.DraftListView.as_view(), name="drafts_list"),
    url('comment/<int:pk>/approve', views.approve_comment, name='approve_comment'),
    url('comment/<int:pk>/delete', views.remove_comment, name='remove_comment'),
    url('', views.PostListView.as_view(), name="post_list"),

]

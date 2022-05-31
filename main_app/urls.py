from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("showList/", views.showList, name="showList"),
    path('about/', views.about, name="about"),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movie_id>/', views.movies_detail, name='detail'),

    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('movies/<int:movie_id>/add_viewing/', views.add_viewing, name='add_viewing'),

    # Comments CRUD operations
    # path('comments/', views.CommentList.as_view(), name="comments_index"),
    path('comments/', views.comments_index, name="comments_index"),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name="comments_detail"),
    path('comments/create/', views.CommentCreate.as_view(), name="comments_create"),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name="comments_update"),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name="comments_delete"),

    path('movies/<int:movie_id>/assoc_comment/<int:comment_id>/', views.assoc_comment, name="assoc_comment"),

    path('accounts/signup/', views.signup, name="signup")


]


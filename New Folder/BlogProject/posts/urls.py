from django.urls import path
from .views import (
    add_post,
    delete_post,
    edit_post,
    AddPostCreateView,
    EditPostView,
    DeletePostView,
)

urlpatterns = [
    # path("add_post/", add_post, name="add_post"),
    path("add_post/", AddPostCreateView.as_view(), name="add_post"),
    # path("delete_post/<int:id>/", delete_post, name="delete_post"),
    path("delete_post/<int:id>/", DeletePostView.as_view(), name="delete_post"),
    # path("edit_post/<int:id>/", edit_post, name="edit_post"),
    path("edit_post/<int:id>/", EditPostView.as_view(), name="edit_post"),
]

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


# Create your views here.
@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.post_author = request.user
            form.save()
            messages.success(request, "Post added successfully.")
            return redirect("add_post")
    else:
        form = PostForm()
    return render(request, "add_post.html", {"form": form})


# add post using class base view
@method_decorator(login_required, name="dispatch")
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    success_url = reverse_lazy("add_post")

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        messages.success(self.request, "Post added successfully.")
        return super().form_valid(form)


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("home")


@method_decorator(login_required, name="dispatch")
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


@login_required
def edit_post(request, id):
    data = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.instance.post_author = request.user
            form.save()
            messages.success(request, "Post edited successfully")
            return redirect("home")
    else:
        form = PostForm(instance=data)
    return render(request, "add_post.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")

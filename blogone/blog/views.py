from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'blog/index.html'

class HomeView(ListView):
    model = Post
    template_name = 'blog/post_list.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'


class PostDeleteView( DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'obj'


class DraftListView(ListView):
    # login_url = '/login/'
    template_name = 'blog/post_draft_list.html'
    redirect_field_name = 'blog/home.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created')


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('home')
    


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class ContactView(TemplateView):
    template_name = 'blog/contact.html'
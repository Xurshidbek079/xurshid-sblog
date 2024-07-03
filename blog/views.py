from django.views.generic import ListView, DetailView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_posts'] = Post.objects.exclude(pk=self.object.pk)
        return context

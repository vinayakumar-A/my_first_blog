from django.shortcuts import render
from .models import Post
from django.views import generic
from django.utils import timezone


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'post_list.html'
    paginate_by = 2

class PostDetail(generic.DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# class ProfileView(generic.ListView):
#     queryset = Profile.objects.all()
#     template_name = 'my_blog/profile.html'

    
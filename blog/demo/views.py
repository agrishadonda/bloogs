from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

# posts = [
#     {
#         'author':'CoreMS',
#         'tital':'Blog Post1',
#         'content':'First post ,content',
#         'date_posted':'October 29 2004'
#     },
#     {
#         'author':'CoreMS',
#         'tital':'Blog Post1',
#         'content':'First post ,content',
#         'date_posted':'October 31 2005'
#     }
# ]
def home(request):
    data = {
        'posts':Post.objects.all()
    }
    return render(request,'home.html',data)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'rec'
    ordering = ['-date_posted']
    paginate_by = 2
    
class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'rec'
    ordering = ['-date_posted']
    paginate_by = 2
    
    
    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(auther = user).order_by('-da')
        
class PostDetailView(DetailView):
    model = Post
  
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['tital','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['tital','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
       
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def about(request):
    return render(request,'about.html',{'tital':'about'})


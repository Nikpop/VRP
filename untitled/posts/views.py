from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, ModelFormMixin
from django.urls import reverse_lazy
import json

from .models import Posts
from .forms import ImageForm

class PostsListView(ListView):
    model = Posts
    template_name = 'posts_list.html'

class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts_detail.html'

class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ('title', 'body')
    template_name = 'posts_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author ==self.request.user


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'posts_delete.html'
    success_url = reverse_lazy('posts_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author ==self.request.user


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'posts_new.html'
    form_class = ImageForm
    login_url = 'login'
    raise_exception = True
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def check_user_name(request):
        if request.GET:
            background = request.GET[""]

    def post(self, request, *args, **kwargs):
        #self.object = None
        #post = super().post(request, *args, **kwargs)
        #return HttpResponse({post.url})
        if request.method == 'POST':
            post = Posts()
            post.title = request.POST.get('title')
            post.body = request.POST.get('body')
            post.background = request.POST.get('background')
            post.terrain = request.POST.get('terrain')
            post.fname = request.POST.get('checkname')
            post.author_id = request.POST.get('author')
            post.posx = float(request.POST.get('posx'))
            post.posy = float(request.POST.get('posy'))
            post.posz = float(request.POST.get('posz'))
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                post.image = request.FILES['image']
                post.save()
                obj = Posts.objects.latest('id')
                response = redirect(obj)
                return response
        else:
            form = ImageForm()
            return render_to_response('/posts_new.html',{'form':form},context_instance=RequestContext(request) )






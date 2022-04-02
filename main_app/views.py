from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie, Comment
from django.views.generic import ListView, DetailView
from .forms import ViewingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = ['title','synopsis','year','image']
  success_url = '/movies/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def movies_index(request):
  movies = Movie.objects.all()
  movies = Movie.objects.filter(user = request.user)
  return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    comments_movie_doesnt_have = Comment.objects.exclude(id__in = movie.comments.all().values_list('id'))
    print(comments_movie_doesnt_have)
    viewing_form = ViewingForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'viewing_form': viewing_form, 'comments': comments_movie_doesnt_have})


def add_viewing(request, movie_id):
  form = ViewingForm(request.POST)
  if form.is_valid():
    new_viewing = form.save(commit=False)
    new_viewing.movie_id = movie_id
    new_viewing.save()
  return redirect('detail', movie_id=movie_id)

class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = '__all__'

class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies/'

class CommentList(LoginRequiredMixin, ListView):
  model = Comment

class CommentDetail(DetailView):
  model = Comment

class CommentCreate(CreateView):
  model = Comment
  fields = '__all__'

class CommentUpdate(UpdateView):
  model = Comment
  fields = '__all__'

class CommentDelete(DeleteView):
  model = Comment
  success_url = '/movies/'

@login_required
def assoc_comment(request, movie_id, comment_id):
    Movie.objects.get(id=movie_id).comments.add(comment_id)
    return redirect('detail', movie_id=movie_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database, see below:
            user = form.save()
            # Then login the user
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid Sign Up. Try Again!"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

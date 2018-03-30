from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .models import Blog,UserProfile,BlogComment
from django.views import generic
from .forms import BlogForm 
from django.shortcuts import get_object_or_404,reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,EditProfileForm,EditUserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm


from django.urls import reverse_lazy


def Home(request):
  
    writers=Blog.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    return render(request,'First.html',context={'writers':writers})
        


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password1=raw_password)
            login(request, user)
            return redirect('First')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def edit_profile(request):

    if request.method =='POST':
        form=EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('First')

    else:
        form=EditProfileForm(instance=request.user)
        args={'forms':form}
        return render(request,'user_change.html', {'form':form})


@login_required
def edit_user_profile(request):
        if request.method =='POST':
            form=EditUserProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('First')

        else:
            form=EditUserProfileForm(instance=request.user)
            args={'forms':form}
            return render(request,'user_profile_change.html', {'form':form})

def profile(request):
    return render(request,'profile.html')

class BlogCreate(LoginRequiredMixin,generic.CreateView):
    model=Blog
    form_class=BlogForm
    # template_name`='blog_form.html'       

    def form_valid(self,form):
    	blog=form.save(commit=False)
    	blog.author=UserProfile.objects.get(user=self.request.user)
    	blog.save()
    	return redirect('/')

class BlogUpdateView(LoginRequiredMixin,generic.UpdateView):
    model=Blog
    fields=['title','content']
    # template_name='blog_update_form.html'
    success_url=reverse_lazy('profile')       

class BlogDeleteView(LoginRequiredMixin,generic.DeleteView):
    model=Blog
    success_url=reverse_lazy('profile')
    template_name='blog_confirm_delete.html'


class BlogListView(LoginRequiredMixin,generic.ListView):
    model=Blog    
    
class BlogDetailView(LoginRequiredMixin,generic.DetailView):
    model =Blog

class UserListView(LoginRequiredMixin,generic.ListView):
    model=UserProfile
    
class UserDetailView(LoginRequiredMixin,generic.DetailView):
    model=UserProfile


class BlogCommentCreate(LoginRequiredMixin, generic.CreateView):
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form): 
       
        form.instance.author =get_object_or_404(UserProfile,user=self.request.user)
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})


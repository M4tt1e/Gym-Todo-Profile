from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import MyOwnSignUpForm, ItemCreateForm, UpdateProfileForm,UpdateUserForm


class ChangePassword(PasswordChangeView):
    template_name = 'todolist/change_password.html'
    success_url = reverse_lazy('todolist:profile')


#if method is post we send data to form (request.POST) but we have an image
# aswell so (request.FILES) sends that
@login_required
def profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance = request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has updated succesfully')
            return HttpResponseRedirect(request.get_full_path())
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'todolist/profile.html', {'user_form':user_form, 'profile_form':profile_form})



class ThisIsMineGTFO(UserPassesTestMixin):
    """
    Allows users that are creators and users that have a shared item with them
    to modify and delete items
    """
    def test_func(self):
        obj = self.get_object()
        return obj.usr == self.request.user or self.request.user in obj.shared_with.all()
    #self.request.user.shared_with_me.filter(id=obj.id).exists()

class SignUpView(generic.CreateView):
    form_class = MyOwnSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class IndexView(generic.ListView):
    """
    Displays all current todo items
    """
    model = Todo
    template_name = 'todolist/index.html'
    context_object_name = 'ordered_todo_items'
    queryset = Todo.objects.order_by('due_date','-importance')


class FinishedItemView(LoginRequiredMixin, generic.ListView):
    """
    Displays all finished items
    """
    model = Todo
    template_name = 'todolist/finished.html'
    context_object_name = 'ordered_todo_items'
    queryset = Todo.objects.order_by('due_date')


class DetailView(LoginRequiredMixin, generic.DetailView):
    """
    Displays a detail page of an item
    """
    model = Todo
    template_name = 'todolist/detail.html'
    context_object_name = 'item'


class EditView(LoginRequiredMixin, ThisIsMineGTFO ,generic.UpdateView):
    """
    Allows each user to modify previously created items
    """
    model = Todo
    fields = ['title', 'body', 'importance', 'due_date', 'finished', 'image']
    template_name = 'todolist/edit.html'
    context_object_name = 'item'
    success_url = reverse_lazy('todolist:index')
    

    def form_valid(self, form):
        lastly = form.instance
        lastly.user_last_change = self.request.user
        return super().form_valid(form)
        


class ItemDeleteView(LoginRequiredMixin, ThisIsMineGTFO, generic.DeleteView):
    """
    Allows each user to delete previously created items
    """
    model = Todo
    template_name = 'todolist/delete.html'
    context_object_name = 'item'
    success_url = reverse_lazy('todolist:index')


class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Allows a user to create a todo item and possibly share it with other
    users
    """
    model = Todo
    template_name = 'todolist/create.html'
    form_class = ItemCreateForm
    context_object_list = 'item'
    success_url = reverse_lazy('todolist:index')

    def form_valid(self, form):
        todo = form.instance
        todo.usr = self.request.user
        todo.save()
        username=form.cleaned_data['share_with']
        obj = get_user_model()
        try:
            obj.objects.get(username=username)
            todo.shared_with.add(
                    obj.objects.get(username=username)
            )
        except get_user_model().DoesNotExist:
            obj = None
        
        return super().form_valid(form)


#class ItemCreateView(generic.TemplateView):
 #   """Non-generic :)"""
  #  template_name = 'todolist/create.html'
#
 #   def dispatch(self, request, *args, **kwargs):
  #      if request.user.is_authenticated:
   #         return super().dispatch(request, *args, **kwargs)
    #    return HttpResponseRedirect(reverse_lazy('login'))
#
 #   def get_context_data(self, **kwargs):
  #      context = super().get_context_data(**kwargs)
   #     context['form'] = ItemCreateForm()
    #    return context
#
 #   def post(self, request, *args, **kwargs):
  #form = ItemCreateForm(data=request.POST)
   #     todo = form.save(commit=False)
    #    todo.usr = self.request.user
     #   todo.save()
      #  return HttpResponseRedirect(reverse_lazy('todolist:index'))

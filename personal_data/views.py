from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import PersonalDataForm, UserForm
from django.shortcuts import render, redirect
from file_worker_app.views import menu, loads, myfiles


class RegisterUser(CreateView):
    form_class = PersonalDataForm
    template_name = 'personal_data/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(menu=menu, **kwargs)
        context['meny'] = menu
        context['loads'] = loads
        context['myfiles'] = myfiles
        context['title'] = 'FileWorker'

        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'personal_data/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(menu=menu, **kwargs)
        context['meny'] = menu
        context['loads'] = loads
        context['myfiles'] = myfiles
        context['title'] = 'FileWorker'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def view_personal_data(request, user_id):
    user = User.objects.get(pk=user_id)
    data = user.personaldata
    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'data': data,
        'user': user
    }
    return render(request, 'personal_data/personal_data.html', context=context)


@transaction.atomic
def edit_personal_data(request, user_id):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        data_form = PersonalDataForm(request.POST, request.FILES,
                                     instance=request.user.personaldata)
        if user_form.is_valid() and data_form.is_valid():
            data_form.save()
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home')

        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        data_form = PersonalDataForm(instance=request.user)

    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'user_form': user_form,
        'profile_form': data_form
    }
    return render(
        request,
        'personal_data/edit_personal_data.html',
        context=context
    )

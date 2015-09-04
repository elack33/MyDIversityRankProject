from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

from .forms import CreateUserForm


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user=form.save()
            user.username=form.cleaned_data['username']
            user.backend='django.contrib.auth.backends.ModelBackend'
            user.save()

            password=str(form.cleaned_data['password1'])
            login(request, user)

            return HttpResponseRedirect(reverse('landing'))

    else:
        form = CreateUserForm()

    return render(
        request,
        'create_user.html',
        context={
            'form': form,
        }
    )


from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render_to_response
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .forms import CreateSurveyResponse
from .models import SurveyResponses
# Create your views here.


def test(request):
    return render(
        request,
        'test.html',
    )


@login_required
def landing(request):
    return render(
        request,
        'landing.html',
    )


@login_required
def manual_entry(request):

    if request.method == 'POST':
        form = CreateSurveyResponse(request.POST)
        if form.is_valid():
            author = request.user
            form.save(author)
            return HttpResponseRedirect(reverse('landing'))

    else:
        form = CreateSurveyResponse()



    return render(
        request,
        'manual_entry.html',
        context={
            'form': form,
        }
    )


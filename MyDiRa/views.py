from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render_to_response, HttpResponse
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
    print 'request user = ', request.user

    if request.method == 'POST':
        form = CreateSurveyResponse(request.POST, author=request.user)
        # print 'before validation'
        print form.is_valid()
        if form.is_valid():
            # print request.user
            author = request.user
            # print 'Before save'
            form.save()
            return HttpResponseRedirect(reverse('manual_entry'))


    else:
        form = CreateSurveyResponse(author=request.user)

    return render(
        request,
        'manual_entry.html',
        context={
            'form': form,
        }
    )


@login_required
def show_data(request):
    author = request.user
    total_surveys = SurveyResponses.objects.filter(author_id=author).count()
    white_people = SurveyResponses.objects.filter(author_id=2, demographic__demographic='White').count()

    return render(
        request,
        'show_data.html',
        context={
            'total': total_surveys,
            'white': white_people
        }
    )



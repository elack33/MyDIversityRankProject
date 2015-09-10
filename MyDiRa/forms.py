from django import forms
from django.contrib.auth.models import User

from .models import Demographics, YearOfBirth, Genders, Interests, Orientations, Careers, Relationship, Ogamy
from .models import Questions, Answer, SurveyResponses, SurveySetup


class CreateSurveyResponse(forms.ModelForm):
    class Meta:
        # app_label = 'SurveyResponses'
        model = SurveyResponses
        fields = '__all__'

        # exclude = [
        #            'interest02',
        #            'interest03',
        #            'interest04',
        #            'interest05',
        #            'interest06',
        #            'interest07',
        #            'interest08',
        #            'interest09',
        #            'interest10',
        #            'career02',
        #            ]

    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', '')
        super(CreateSurveyResponse, self).__init__(*args, **kwargs)
        self.fields['author'].widget=forms.HiddenInput()
        self.fields['author'].initial=author






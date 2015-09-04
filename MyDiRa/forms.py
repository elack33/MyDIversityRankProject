from django import forms

from .models import Demographics, YearOfBirth, Genders, Interests, Orientations, Careers, Relationship, Ogamy
from .models import Questions, Answer, SurveyResponses, SurveySetup


class CreateSurveyResponse(forms.ModelForm):
    class Meta:
        model = SurveyResponses
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(CreateSurveyResponse, self).__init__(*args, **kwargs)
        self.fields['Demographics'] = forms.ModelChoiceField(queryset=Demographics.objects.all())
        self.fields['YearOfBirth'] = forms.ModelChoiceField(queryset=YearOfBirth.objects.all().order_by('year'))
        self.fields['Genders'] = forms.ModelChoiceField(queryset=Genders.objects.all().order_by('gender'))
        self.fields['Interests'] = forms.ModelChoiceField(queryset=Interests.objects.all().order_by('interest'))
        self.fields['Orientations'] = forms.ModelChoiceField(queryset=Orientations.objects.all())
        self.fields['Careers'] = forms.ModelChoiceField(queryset=Careers.objects.all().order_by('career'))
        self.fields['Relationship'] = forms.ModelChoiceField(queryset=Relationship.objects.all())
        self.fields['Ogamy'] = forms.ModelChoiceField(queryset=Ogamy.objects.all().order_by('title'))

    def save(self, author):
        new_response = super(CreateSurveyResponse, self).save()
        new_response.author = author
        new_response.demographic = self.cleaned_data.get('Demographics')
        print type(self.cleaned_data.get('Demographics'))
        new_response.year = self.cleaned_data.get('YearOfBirth')
        new_response.genders = self.cleaned_data.get('Genders')
        new_response.interests = self.cleaned_data.get('Interests')
        new_response.orientations = self.cleaned_data.get('Orientations')
        new_response.careers = self.cleaned_data.get('Careers')
        new_response.relationship = self.cleaned_data.get('Relationship')
        new_response.ogamy = self.cleaned_data.get('Ogamy')
        print new_response
        new_response.save()
        return new_response



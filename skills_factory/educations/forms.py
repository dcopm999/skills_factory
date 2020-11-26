from django import forms

from skills_factory.educations import models


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer

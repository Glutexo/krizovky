from django import forms

from .models import CrosswordAnswer, SourceURL


class CrosswordAnswerForm(forms.ModelForm):
    class Meta:
        model = CrosswordAnswer
        fields = ["text", "source_url"]


class SourceURLForm(forms.ModelForm):
    class Meta:
        model = SourceURL
        fields = ["url"]

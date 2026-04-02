from django import forms

from .models import CrosswordAnswer, SourceURL


class CrosswordAnswerForm(forms.ModelForm):
    source_url_value = forms.URLField(label="Zdrojová URL", required=False)

    class Meta:
        model = CrosswordAnswer
        fields = ["text"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if self.instance.pk and self.instance.source_url_id:
            self.fields["source_url_value"].initial = self.instance.source_url.url

    def save(self, commit: bool = True) -> CrosswordAnswer:
        source_url_value = self.cleaned_data["source_url_value"].strip()
        if source_url_value:
            source_url, _ = SourceURL.objects.get_or_create(url=source_url_value)
            self.instance.source_url = source_url
        else:
            self.instance.source_url = None
        return super().save(commit=commit)

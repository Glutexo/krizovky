from django import forms

from .models import Tajenka, ZdrojovaURL


class TajenkaForm(forms.ModelForm):
    source_url = forms.URLField(label="Zdrojová URL")

    class Meta:
        model = Tajenka
        fields = ["text", "source_url"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields["source_url"].initial = self.instance.source.url

    def save(self, commit: bool = True) -> Tajenka:
        source_url = self.cleaned_data["source_url"]
        source, _ = ZdrojovaURL.objects.get_or_create(url=source_url)

        self.instance.source = source
        return super().save(commit=commit)

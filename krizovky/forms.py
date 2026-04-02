from django import forms
from django.db.models import Q

from .models import CrosswordAnswer, SourceURL


class CrosswordAnswerForm(forms.ModelForm):
    class Meta:
        model = CrosswordAnswer
        fields = ["text", "source_url"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        queryset = SourceURL.objects.all()
        if self.instance.pk and self.instance.source_url_id:
            queryset = SourceURL.all_objects.filter(
                Q(pk=self.instance.source_url_id) | Q(deleted_at__isnull=True)
            ).order_by("url")

        self.fields["source_url"].queryset = queryset


class SourceURLForm(forms.ModelForm):
    class Meta:
        model = SourceURL
        fields = ["url"]

    def save(self, commit: bool = True) -> SourceURL:
        url = self.cleaned_data["url"]
        existing = SourceURL.all_objects.filter(url=url).first()

        if existing and existing.pk != self.instance.pk:
            existing.deleted_at = None
            if commit:
                existing.save(update_fields=["deleted_at", "updated_at"])
            return existing

        return super().save(commit=commit)

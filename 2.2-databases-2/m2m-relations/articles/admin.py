from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scopes

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        tags = {}
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                i += 1
            tag = str(form.cleaned_data.get('tag', ''))
            deleting = form.cleaned_data.get('DELETE', False)
            if tag and not deleting:
                tags[tag] = tags.get(tag, 0) + 1
        repeating_tags = [t for t in tags.keys() if tags[t] > 1]
        if repeating_tags:
            raise ValidationError(f'Недопустимо повторение разделов ({", ".join(repeating_tags)})')
        if i != 1:
            raise ValidationError(f'Один раздел должен быть основным. У Вас - {i}!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopesInline(admin.TabularInline):
    model = Scopes
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ScopesInline,)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


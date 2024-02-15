from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article,Tag, Scope

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class RelationshipInlineFormset (BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
        if count == 1:
            return super().clean()
        else:
            if count == 0:
                raise ValidationError('Укажите основной раздел')
            else:
                raise ValidationError('Основным может быть только один раздел')
class ScopeInLine(admin.TabularInline):
    model = Scope
    fields = ['tag', 'is_main']
    formset = RelationshipInlineFormset
    extra = 3


#@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]

admin.site.register(Article,ArticleAdmin)

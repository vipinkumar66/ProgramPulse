from typing import Any
from django import forms
from django.shortcuts import get_object_or_404
from blog.models import Article, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    new_category = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "w-[90%] text-semibold h-[2rem] py-2 px-1"
    }), help_text="Add comma (,) if you want to add multiple fields", label="Add Category")
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            "class": "w-[90%] px-2 py-4 font-semibold text-md rounded-lg item-start"
        }),
        empty_label="Select a Category"
    )

    class Meta:
        model = Article
        fields = ["title", "content", "category", "new_category"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-[90%] px-2 py-4 font-semibold text-md rounded-lg item-start"
            }),
        }

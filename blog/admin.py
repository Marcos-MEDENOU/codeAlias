from django.contrib import admin
from django import forms
from blog.models import Post


# from django import models
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget
# Register your models here.

from django.contrib.auth.models import User
# admin.site.unregister(User)
@admin.register(Post)
class CustomAdminClass(ModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = False

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    formfield_overrides = {
        models.TextField: {
            "widget": forms.Textarea(attrs={'id': "richtext_field"}),
        },
        ArrayField: {
            "widget": ArrayWidget,
        }
    }


class CustomAdminClass(ModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = False

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    formfield_overrides = {
        models.TextField: {
            "widget": forms.Textarea(attrs={'id': "richtext_field"}),
        },
        ArrayField: {
            "widget": ArrayWidget,
        }
    }

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Post
        fields = "__all__"

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    BlogCategoryModel,
    BlogTagModel,
    BlogAuthorModel,
    BlogModel,
    BlogCommentModel,
)

class MyTranslationAdmin(TranslationAdmin):
        class Media:
            js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
            }

@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(MyTranslationAdmin):
    list_display = ('id', 'title', 'parent',)
    search_fields = ('title',)
    list_filter = ('parent',)


@admin.register(BlogTagModel)
class BlogTagAdmin(MyTranslationAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(BlogAuthorModel)
class BlogAuthorAdmin(MyTranslationAdmin):
    list_display = ('id', 'get_full_name', 'avatar')
    search_fields = ('first_name', 'last_name')

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = "Full Name"

@admin.register(BlogModel)
class BlogAdmin(MyTranslationAdmin):
    list_display = ('id', 'title', 'image', 'created_at')
    search_fields = ('title',)
    list_filter = ('categories', 'author')

@admin.register(BlogCommentModel)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'user')
    search_fields = ('comment', 'user__username')

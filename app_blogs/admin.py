from django.contrib import admin
from .models import (
    BlogCategoryModel,
    BlogTagModel,
    BlogAuthorModel,
    BlogModel,
    BlogCommentModel,
)

# Register BlogCategoryModel
@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')
    search_fields = ('title',)
    list_filter = ('parent',)

# Register BlogTagModel
@admin.register(BlogTagModel)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

# Register BlogAuthorModel
@admin.register(BlogAuthorModel)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'avatar')
    search_fields = ('first_name', 'last_name')

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = "Full Name"

# Register BlogModel
@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description')
    search_fields = ('title',)
    list_filter = ('categories', 'author')

# Register BlogCommentModel
@admin.register(BlogCommentModel)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'user')
    search_fields = ('comment', 'user__username')

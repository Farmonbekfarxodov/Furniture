from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.BlogCategoryModel)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(models.BlogTagModel)
class BlogTagTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(models.BlogAuthorModel)
class BlogAuthorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)

@register(models.BlogModel)
class BlogModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

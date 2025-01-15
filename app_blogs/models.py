from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel

UserModel = get_user_model()

class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128)
    parent = models.ForeignKey('self',on_delete=models.PROTECT,null=True,blank=True,related_name='children')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'blog category'
        verbose_name_plural = 'blog categories'
    
class BlogTagModel(BaseModel):
    title = models.CharField(max_length=128)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'blog tag'
        verbose_name_plural = 'blog tags'

class BlogAuthorModel(BaseModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='blogs/authors/')

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"
    
    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        verbose_name = 'blog author'
        verbose_name_plural = 'blog authors'

class BlogModel(BaseModel):
    image = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=128)
    description = models.TextField()

    author = models.ManyToManyField(BlogAuthorModel,related_name='blogs')
    categories = models.ManyToManyField(BlogCategoryModel,related_name='blogs')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

class BlogCommentModel(BaseModel):
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='blog_comments')


    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'blog comment'
        verbose_name_plural = 'blog comments'

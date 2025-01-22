from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['full_name','subject','created_at']
    search_fields = ['message','subject']
    list_filter = ['created_at']
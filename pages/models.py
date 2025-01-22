from django.db import models

from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128,verbose_name=_("full_name"))
    email = models.EmailField(verbose_name=_("message"))
    subject = models.CharField(max_length=255,verbose_name=_("subject"))
    message = models.TextField(verbose_name=_("message"))


    def __str__(self):
        return f"{self.full_name},{self.subject}"
    
    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

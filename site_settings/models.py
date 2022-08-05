from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel

@register_setting
class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(
        blank=True,
        help_text='Enter your Facebook URL',
    )
    twitter = models.URLField(
        blank=True,
        help_text='Enter your Twitter URL',
    )
    youtube = models.URLField(
        blank=True,
        help_text='Enter your Youtube URL',
    )
    instagram = models.URLField(
        blank=True,
        help_text='Enter your Instagram URL',
    )

    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("youtube"),
        FieldPanel("instagram"),
    ]

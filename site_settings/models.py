

from modelcluster.models import models


class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(
        blank=True,
        help_text='Enter your ____ URL',
    )
    twitter = models.URLField(
        blank=True,
        help_text='Enter your ____ URL',
    )
    youtube = models.URLField(
        blank=True,
        help_text='Enter your ____ URL',
    )
    instagram = models.URLField(
        blank=True,
        help_text='Enter your ____ URL',
    )

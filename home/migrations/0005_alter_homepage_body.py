# Generated by Django 4.0.5 on 2022-07-14 12:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 charactes.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='image will be automagically cropped 570px by 370px'))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]

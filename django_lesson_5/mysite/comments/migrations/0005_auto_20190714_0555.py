# Generated by Django 2.2.2 on 2019-07-14 05:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20190710_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]

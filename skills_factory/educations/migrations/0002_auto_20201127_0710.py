# Generated by Django 3.0.11 on 2020-11-27 07:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cource',
            name='desc',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='desc',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='video',
            name='desc',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
    ]

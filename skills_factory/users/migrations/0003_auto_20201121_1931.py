# Generated by Django 3.0.11 on 2020-11-21 19:31

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201121_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='user-images', verbose_name='User image'),
        ),
    ]
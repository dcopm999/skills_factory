# Generated by Django 3.0.11 on 2020-11-21 14:14

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='', upload_to='user-images', verbose_name='User image'),
            preserve_default=False,
        ),
    ]

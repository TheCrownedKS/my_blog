# Generated by Django 3.0.11 on 2021-01-04 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0003_auto_20210104_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='cover',
        ),
    ]

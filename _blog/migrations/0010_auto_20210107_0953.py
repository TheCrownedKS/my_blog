# Generated by Django 3.0.11 on 2021-01-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0009_auto_20210107_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='fb_link',
        ),
        migrations.RemoveField(
            model_name='author',
            name='ist_link',
        ),
        migrations.RemoveField(
            model_name='author',
            name='tw_link',
        ),
        migrations.AddField(
            model_name='author',
            name='facebook',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='instagram',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

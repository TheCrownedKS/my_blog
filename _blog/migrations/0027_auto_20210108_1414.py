# Generated by Django 3.0.11 on 2021-01-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0026_auto_20210108_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='lien facebook'),
        ),
    ]

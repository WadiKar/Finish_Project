# Generated by Django 4.1.3 on 2022-12-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='title',
            field=models.TextField(default=False, max_length=200),
            preserve_default=False,
        ),
    ]

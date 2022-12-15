# Generated by Django 4.1.3 on 2022-12-15 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='author_specialist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='release',
            name='category_release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='media.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='media.category'),
        ),
        migrations.AddField(
            model_name='audiobook',
            name='authors',
            field=models.ManyToManyField(related_name='audiobooks', to='media.author'),
        ),
        migrations.AddField(
            model_name='audiobook',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='media.book'),
        ),
        migrations.AddField(
            model_name='audiobook',
            name='categories',
            field=models.ManyToManyField(to='media.category'),
        ),
    ]

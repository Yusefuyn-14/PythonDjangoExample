# Generated by Django 3.2.9 on 2023-07-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_slug_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug_field',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

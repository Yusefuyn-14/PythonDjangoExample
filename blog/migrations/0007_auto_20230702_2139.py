# Generated by Django 3.2.9 on 2023-07-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_slug_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug_field',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]

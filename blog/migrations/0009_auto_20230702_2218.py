# Generated by Django 3.2.9 on 2023-07-02 22:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20230702_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='contents',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 3.2.9 on 2023-06-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='page_type',
            field=models.CharField(default='blog/partials/blog_card_2.html', max_length=200),
        ),
    ]

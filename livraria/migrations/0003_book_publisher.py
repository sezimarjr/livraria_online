# Generated by Django 5.1.1 on 2024-09-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0002_alter_author_name_alter_category_name_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

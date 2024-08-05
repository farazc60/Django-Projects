# Generated by Django 5.0.7 on 2024-08-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
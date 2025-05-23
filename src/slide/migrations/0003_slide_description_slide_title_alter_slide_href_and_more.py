# Generated by Django 5.2.1 on 2025-05-20 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0002_slide_href_slide_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='description',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='href',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='text',
            field=models.CharField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.1.7 on 2019-02-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.TextField(max_length=1000),
        ),
    ]

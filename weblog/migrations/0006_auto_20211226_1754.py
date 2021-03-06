# Generated by Django 3.2.9 on 2021-12-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0005_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-27 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]

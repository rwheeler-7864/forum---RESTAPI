# Generated by Django 2.2.2 on 2019-06-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='promocode',
            field=models.TextField(default='123457', max_length=10),
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-09 02:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_remove_post_promocode'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='promocode',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100),
        ),
    ]
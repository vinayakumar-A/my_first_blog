# Generated by Django 3.1.2 on 2020-11-01 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
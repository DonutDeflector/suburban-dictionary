# Generated by Django 2.0.7 on 2018-08-08 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suburban_dictionary', '0007_auto_20180805_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='definition',
            name='edited_date',
        ),
    ]

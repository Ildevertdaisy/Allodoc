# Generated by Django 3.2.3 on 2021-06-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]
# Generated by Django 2.0.4 on 2018-04-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20180426_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='cover_letter',
            field=models.TextField(max_length=100, null=True),
        ),
    ]

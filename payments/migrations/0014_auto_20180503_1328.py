# Generated by Django 2.0.4 on 2018-05-03 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0013_auto_20180502_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='total_amount',
        ),
    ]

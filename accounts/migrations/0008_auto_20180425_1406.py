# Generated by Django 2.0.4 on 2018-04-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180424_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
    ]

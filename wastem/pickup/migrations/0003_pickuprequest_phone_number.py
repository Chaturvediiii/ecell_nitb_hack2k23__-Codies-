# Generated by Django 4.1.6 on 2023-02-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickup', '0002_pickuprequest_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickuprequest',
            name='phone_number',
            field=models.CharField(default='+91', max_length=20),
        ),
    ]
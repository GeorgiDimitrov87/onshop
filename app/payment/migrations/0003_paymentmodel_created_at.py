# Generated by Django 4.1 on 2022-08-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_paymentmodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 4.0.4 on 2022-08-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_payment_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Teamname',
            field=models.CharField(default=True, max_length=80),
        ),
        migrations.AddField(
            model_name='payment',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]

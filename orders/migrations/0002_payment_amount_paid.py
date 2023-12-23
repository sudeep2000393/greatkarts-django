# Generated by Django 5.0 on 2023-12-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
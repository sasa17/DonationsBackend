# Generated by Django 2.2.7 on 2020-03-31 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200331_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]

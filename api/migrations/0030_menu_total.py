# Generated by Django 2.2.10 on 2020-04-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20200402_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

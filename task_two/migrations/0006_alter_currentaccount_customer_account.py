# Generated by Django 3.2.9 on 2022-08-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_two', '0005_alter_currentaccount_customer_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentaccount',
            name='customer_account',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

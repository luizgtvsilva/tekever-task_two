# Generated by Django 3.2.9 on 2022-08-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_two', '0007_auto_20220801_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]

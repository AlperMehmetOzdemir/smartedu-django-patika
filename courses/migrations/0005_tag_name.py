# Generated by Django 3.2.8 on 2021-11-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20211102_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
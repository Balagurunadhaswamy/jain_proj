# Generated by Django 5.1 on 2024-09-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]

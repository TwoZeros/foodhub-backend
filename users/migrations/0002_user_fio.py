# Generated by Django 2.2.9 on 2020-01-25 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

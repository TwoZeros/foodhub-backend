# Generated by Django 2.2.9 on 2020-01-07 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_merge_20200107_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='status_client',
            name='color',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='status_client',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
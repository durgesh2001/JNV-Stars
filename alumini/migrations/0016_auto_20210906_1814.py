# Generated by Django 3.1.5 on 2021-09-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumini', '0015_auto_20210906_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluminies',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

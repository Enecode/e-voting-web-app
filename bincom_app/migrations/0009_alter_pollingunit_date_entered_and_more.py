# Generated by Django 4.2.2 on 2023-06-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom_app', '0008_alter_ward_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='date_entered',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ward',
            name='date_entered',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]

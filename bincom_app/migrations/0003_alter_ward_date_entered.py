# Generated by Django 4.2.2 on 2023-06-06 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom_app', '0002_alter_ward_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='date_entered',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-06 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom_app', '0004_alter_ward_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='ward_description',
            field=models.TextField(max_length=255),
        ),
    ]

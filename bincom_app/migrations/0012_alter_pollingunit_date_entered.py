# Generated by Django 4.2.2 on 2023-06-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom_app', '0011_alter_pollingunit_user_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='date_entered',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]

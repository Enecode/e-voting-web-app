# Generated by Django 4.2.2 on 2023-06-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom_app', '0010_alter_pollingunit_polling_unit_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='user_ip_address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom_app', '0015_alter_pollingunit_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='user_ip_address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
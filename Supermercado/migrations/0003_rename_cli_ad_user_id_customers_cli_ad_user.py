# Generated by Django 4.1 on 2022-09-30 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Supermercado', '0002_rename_cli_ad_user_customers_cli_ad_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='CLI_AD_User_id',
            new_name='CLI_AD_User',
        ),
    ]
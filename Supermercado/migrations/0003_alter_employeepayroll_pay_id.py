# Generated by Django 4.1 on 2022-09-13 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supermercado', '0002_alter_administrator_ad_password_alter_business_em_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeepayroll',
            name='PAY_Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

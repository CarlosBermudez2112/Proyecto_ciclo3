# Generated by Django 4.1 on 2022-09-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supermercado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='AD_PASSWORD',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='business',
            name='EM_ID',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='business',
            name='EM_NIT',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='EMP_PASSWORD',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='EGR_Total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='ING_Code',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='ING_Quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='ING_Total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='typeexpenses',
            name='TEGR_NameExpenses',
            field=models.IntegerField(unique=True),
        ),
    ]
# Generated by Django 3.0.3 on 2020-03-05 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20200304_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinventory',
            name='intprop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Store'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-05 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0007_auto_20200305_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeinventory',
            options={'ordering': ['intprop', 'dblcurrentrate', 'strSpecial']},
        ),
    ]

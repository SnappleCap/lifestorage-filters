# Generated by Django 3.0.3 on 2020-03-07 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0009_auto_20200305_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='intprop',
            new_name='storeid',
        ),
    ]

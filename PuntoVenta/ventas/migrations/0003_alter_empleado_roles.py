# Generated by Django 5.0.2 on 2024-03-20 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ventas', '0002_remove_empleado_roles_empleado_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='roles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]

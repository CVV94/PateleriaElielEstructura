# Generated by Django 4.2.7 on 2023-12-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceAdmin', '0003_alter_presentacionproducto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(db_column='TIPO', max_length=100),
        ),
    ]
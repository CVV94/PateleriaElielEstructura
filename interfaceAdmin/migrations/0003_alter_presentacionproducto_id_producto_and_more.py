# Generated by Django 4.2.3 on 2023-12-13 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceAdmin', '0002_carritocompra_cliente_compra_estadoenvio_estadopago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacionproducto',
            name='id_producto',
            field=models.ForeignKey(db_column='ID_PRODUCTO', on_delete=django.db.models.deletion.DO_NOTHING, related_name='presentaciones', to='interfaceAdmin.producto'),
        ),
        migrations.AlterField(
            model_name='valor',
            name='id_producto',
            field=models.ForeignKey(db_column='ID_PRODUCTO', on_delete=django.db.models.deletion.DO_NOTHING, related_name='valores', to='interfaceAdmin.producto'),
        ),
    ]

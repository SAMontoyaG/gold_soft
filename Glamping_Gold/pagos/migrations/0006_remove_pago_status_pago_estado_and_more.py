# Generated by Django 5.0.2 on 2024-03-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0005_alter_pago_fecha_alter_pago_reserva_alter_pago_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='status',
        ),
        migrations.AddField(
            model_name='pago',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='metodo_pago',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pago',
            name='valor',
            field=models.FloatField(max_length=50),
        ),
    ]

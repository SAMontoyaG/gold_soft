
# Generated by Django 4.2.7 on 2024-03-05 14:38

# Generated by Django 4.2.7 on 2024-03-05 20:05


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservas', '0007_rename_valor_reserva_precio'),
        ('cabañas', '0002_rename_tipo_cabaña_cabaña_tipocabaña_and_more'),

        ('reservas', '0007_rename_valor_reserva_precio'),

    ]

    operations = [
        migrations.CreateModel(
            name='Reserva_cabaña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_C', models.IntegerField()),
                ('id_cabaña', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cabañas.cabaña')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservas.reserva')),
            ],
        ),
    ]

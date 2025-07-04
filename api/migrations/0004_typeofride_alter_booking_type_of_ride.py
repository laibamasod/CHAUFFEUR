# Generated by Django 4.2.23 on 2025-06-28 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_childseat_total_price_alter_childseat_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='type_of_ride',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='api.typeofride'),
        ),
    ]

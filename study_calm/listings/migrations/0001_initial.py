# Generated by Django 2.2.3 on 2019-07-05 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('geo_lat', models.DecimalField(decimal_places=17, default=37.556097, max_digits=20)),
                ('geo_lng', models.DecimalField(decimal_places=17, default=126.942911, max_digits=20)),
                ('listing_type', models.CharField(choices=[('kyo', '교습소'), ('acd', '학원'), ('std', '독서실')], default='acd', max_length=3)),
                ('operational_hours_24', models.BooleanField(default=False)),
                ('operational_hours_start', models.CharField(max_length=5)),
                ('operational_hours_end', models.CharField(max_length=5)),
                ('rent_room', models.BooleanField(default=False)),
                ('rent_room_total', models.IntegerField(default=0)),
                ('rent_room_available', models.IntegerField(default=0)),
                ('rent_seat', models.BooleanField(default=False)),
                ('rent_seat_total', models.IntegerField(default=0)),
                ('rent_seat_available', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Supplier')),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
                'db_table': 'Listings',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('act_type', models.CharField(choices=[('room', 'Room'), ('seat', 'Seat'), ('all', 'All Category')], max_length=4)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('long_name_kr', models.CharField(max_length=50)),
                ('long_name_en', models.CharField(max_length=80)),
                ('detail', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Listing Service Detail',
                'verbose_name_plural': 'Listing Service Details',
                'db_table': 'Prod_Details',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nth_seat', models.IntegerField()),
                ('extendable', models.BooleanField(default=True)),
                ('in_use', models.BooleanField(default=True)),
                ('in_use_until', models.DateTimeField()),
                ('details', models.ManyToManyField(to='listings.ProductDetail')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
                ('used_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Seat',
                'verbose_name_plural': 'Seats',
                'db_table': 'Seats',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nth_room', models.IntegerField()),
                ('max_pax', models.IntegerField()),
                ('min_pax', models.IntegerField()),
                ('extendable', models.BooleanField(default=True)),
                ('in_use', models.BooleanField(default=True)),
                ('in_use_until', models.DateTimeField()),
                ('details', models.ManyToManyField(to='listings.ProductDetail')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
                ('used_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'db_table': 'Rooms',
            },
        ),
    ]
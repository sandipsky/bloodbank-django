# Generated by Django 4.1.7 on 2023-03-07 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=20, null=True)),
                ('unit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=500)),
                ('bloodgroup', models.CharField(max_length=3)),
                ('in_stock', models.BooleanField(default=True, null=True)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('requester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='BloodDonate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.donor')),
            ],
        ),
    ]

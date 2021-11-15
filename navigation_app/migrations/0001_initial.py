# Generated by Django 3.2.9 on 2021-11-15 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='NavigationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=12)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigation_app.vehicle')),
            ],
        ),
    ]

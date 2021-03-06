# Generated by Django 3.2 on 2021-04-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dna', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='simiosXHumanos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simios', models.PositiveIntegerField(default=0)),
                ('humanos', models.PositiveIntegerField(default=0)),
                ('ratio', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
            ],
        ),
    ]

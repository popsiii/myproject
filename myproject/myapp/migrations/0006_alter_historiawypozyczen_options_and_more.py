# Generated by Django 5.1.2 on 2025-01-21 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_historiawypozyczen_wypozyczenia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historiawypozyczen',
            options={'verbose_name': 'Historia wypożyczeń', 'verbose_name_plural': 'Historia wypożyczeń'},
        ),
        migrations.AlterModelOptions(
            name='wypozyczenia',
            options={'verbose_name': 'Wypożyczenie', 'verbose_name_plural': 'Wypożyczenia'},
        ),
        migrations.AlterField(
            model_name='historiawypozyczen',
            name='ksiazka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historia_wypozyczen', to='myapp.ksiazka'),
        ),
        migrations.AlterField(
            model_name='historiawypozyczen',
            name='uzytkownik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historia_wypozyczen', to='myapp.uzytkownik'),
        ),
        migrations.AlterField(
            model_name='wypozyczenia',
            name='ksiazka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ksiazka'),
        ),
        migrations.AlterField(
            model_name='wypozyczenia',
            name='uzytkownik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.uzytkownik'),
        ),
    ]
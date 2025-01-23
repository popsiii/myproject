# Generated by Django 5.1.1 on 2025-01-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_historiawypozyczen_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historiawypozyczen',
            options={'verbose_name': 'Historia Wypożyczeń', 'verbose_name_plural': 'Historia Wypożyczeń'},
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='plec',
            field=models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inna'), (4, 'Nie Chcę Podawać')], default=1),
        ),
    ]

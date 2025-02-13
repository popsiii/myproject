from datetime import date
from django.utils.timezone import now
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager

PLEC = models.IntegerChoices('Płeć', 'Kobieta Mężczyzna Inna Nie_chcę_podawać')

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Uzytkownik(AbstractUser):
    username = None 
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    plec = models.IntegerField(choices=PLEC.choices, default=PLEC.Kobieta)  
    data_dodania = models.DateField(default=date.today, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['imie', 'nazwisko', 'plec']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.email})"

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"


WYDAWNICTWA = models.IntegerChoices(
    'Wydawnictwo',
    'Inne'
    'Agencja_Dramatu_i_Teatru '
    'Agencja_Wydawnicza_Runa '
    'Agencja_Wydawniczo_Reklamowa_Skarpa_Warszawska '
    'Alkazar '
    'Alma_Press '
    'Ameet '
    'Franciszkańskie_Wydawnictwo_św_Antoniego '
    'ArtRage '
    'Bellona '
    'Biały_Kruk '
    'Biuro_Literackie '
    'Bogucki_Wydawnictwo_Naukowe '
    'CIA_Books '
    'Convivo '
    'Czuły_Barbarzyńca_Press '
    'Dom_Literatury_w_Łodzi '
    'Dom_Wydawniczy_Elipsa '
    'Dom_Wydawniczy_Rebis '
    'Doświadczalna_Oficyna_Graficzna '
    'Drzewo_Babel '
    'Edycja_Świętego_Pawła '
    'Elamed_Media_Group '
    'Elay '
    'Eneteia_Wydawnictwo_Szkolenia '
    'EscapeMagazine_pl '
    'Fabryka_Słów '
    'Flos_Carmeli '
    'Fundacja_Duży_Format '
    'Fundacja_Festina_Lente '
    'Fundacja_Instytut_Wydawniczy_Książka_i_Presa '
    'Gdańskie_Wydawnictwo_Psychologiczne '
    'Gebethner_i_Wolff '
    'Genius_Creations '
    'Hejnał '
    'Homo_Dei '
    'Towarzystwo_Wydawnicze_Ignis '
    'Inforteditions '
    'Insignis_Media '
    'Instytut_im_Oskara_Kolberga '
    'Instytut_Wydawniczy_Pax '
    'Instytut_Wydawniczy_Latarnik '
    'ISA '
    'Wydawnictwo_Kle '
    'Klub_dla_Ciebie '
    'Kolegium_Europy_Wschodniej_im_Jana_Nowaka_Jeziorańskiego '
    'Krakowska_Spółka_Wydawnicza '
    'Książka_i_Wiedza '
    'Książnica_Atlas '
    'Księgarnia_Akademicka '
    'Księży_Młyn_Dom_Wydawniczy '
    'Kurhaus_Publishing '
    'Wydawnictwo_Kusiński '
    'Lampa_i_Iskra_Boża '
    'Wydawnictwo_Literackie '
    'Wydawnictwo_Literatura '
    'Ludowa_Spółdzielnia_Wydawnicza '
    'Ładne_Halo '
    'Mamiko '
    'Marpress '
    'Media_Rodzina '
    'Młodzieżowa_Agencja_Wydawnicza '
    'Muza '
    'Mystic_Production '
    'Neriton '
    'Wydawnictwo_Nisza '
    'Noir_sur_Blanc '
    'Norbertinum '
    'Wydawnictwo_Novae_Res '
    'Nowy_Świat '
    'Wydawnictwo_Officyna '
    'Oficyna_21 '
    'Okultura '
    'Państwowy_Instytut_Wydawniczy '
    'Phantom_Press '
    'Polskie_Książki_Telefoniczne '
    'Polskie_Przedsiębiorstwo_Wydawnictw_Kartograficznych '
    'Polskie_Wydawnictwo_Ekonomiczne '
    'Powszechne_Wydawnictwo_Rolnicze_i_Leśne '
    'Presscom '
    'Prodoks '
    'Prószyński_i_Ska '
    'Rosikon_Press '
    'Towarzystwo_Wydawnicze_Rój '
    'Wydawnictwo_Salwator '
    'Słowo_Prawdy '
    'Słowo_obraz_terytoria '
    'Smak_Słowa '
    'Społeczny_Instytut_Wydawniczy_Znak '
    'Spółdzielnia_Wydawnicza_Czytelnik '
    'Spółdzielnia_Wydawnicza_Książka '
    'Wydawnictwo_Stalker_Books '
    'Stowarzyszenie_Salon_Literacki '
    'Świat_Książki '
    'Tern_Book '
    'Towarzystwo_Autorów_i_Wydawców_Prac_Naukowych_Universitas '
    'W_drodze '
    'WarBook '
    'Wiedza_i_Praktyka '
    'Wydawnictwo_Wolno '
    'Wolters_Kluwer_Polska '
)

OKLADKA = models.IntegerChoices('okładka', 'twarda miękka')

class Gatunek(models.Model):
    nazwa_gatunku = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa_gatunku
    
    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"

class Autor(models.Model): 
    imie_autora = models.CharField(max_length=100)
    nazwisko_autora = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.imie_autora} {self.nazwisko_autora}" 
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.ManyToManyField(Autor)
    wydawnictwo = models.IntegerField(choices=WYDAWNICTWA.choices)
    rok_wydania = models.CharField(max_length=4)
    liczba_stron = models.IntegerField()
    ISBN = models.CharField(max_length=13)  
    okładka = models.IntegerField(choices=OKLADKA.choices)
    gatunek = models.ManyToManyField(Gatunek)

    def __str__(self):
        autorzy = ", ".join([str(autor) for autor in self.autor.all()])  # Pobranie listy autorów
        return f'"{self.tytul}" by {autorzy} ({self.rok_wydania})'
    
    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"



class Wypozyczenia(models.Model):
    uzytkownik = models.ForeignKey('Uzytkownik', on_delete=models.CASCADE)
    ksiazka = models.ForeignKey('Ksiazka', on_delete=models.CASCADE)
    data_wypozyczenia = models.DateField(default=now, verbose_name="Data wypożyczenia")

    def __str__(self):
        return f'{self.uzytkownik} wypożyczył/a "{self.ksiazka.tytul}" w dniu {self.data_wypozyczenia.strftime("%Y-%m-%d")}'

    def zwroc_ksiazke(self):
        HistoriaWypozyczen.objects.create(
            uzytkownik=self.uzytkownik,
            ksiazka=self.ksiazka,
            data_wypozyczenia=self.data_wypozyczenia,
            data_zwrotu=now()
        )
        self.delete()

    class Meta:
        verbose_name = "Wypożyczenie"
        verbose_name_plural = "Wypożyczenia"

class HistoriaWypozyczen(models.Model):
    uzytkownik = models.ForeignKey('Uzytkownik', on_delete=models.SET_NULL, null=True, related_name='historia_wypozyczen')
    ksiazka = models.ForeignKey('Ksiazka', on_delete=models.SET_NULL, null=True, related_name='historia_wypozyczen')
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField(default=now)

    def __str__(self):
        return f'{self.uzytkownik} zwrócił/a "{self.ksiazka.tytul}" w dniu {self.data_zwrotu.strftime("%Y-%m-%d")}'

    class Meta:
        verbose_name = "Historia Wypożyczeń"
        verbose_name_plural = "Historia Wypożyczeń"
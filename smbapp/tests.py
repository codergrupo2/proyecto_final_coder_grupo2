from django.test import TestCase
from smbapp.forms import * # usado para testear los formularios

# Create your tests here.
class TestingBand(TestCase):
    
    # Se requiere la imagen antes de crear la banda
    def test_band_image_required(self):
        form = FormCreateBand(data={
            'name' : 'Mi banda', 
            'tour_dates' : '2022-12-25', 
            'image' : 'Mi_imagen', 
            'artist_info' : 'Informacion del artista aqui'
        })
        self.assertEquals(form.errors["image"], ['This field is required.'])
    
    # Se requiere la fecha en el formato correcto
    def test_wrong_date(self):
        form = FormCreateBand(data={
            'name' : 'Mi banda', 
            'tour_dates' : 'a5s1d6a5', 
            'image' : 'Mi_imagen', 
            'artist_info' : 'Informacion del artista aqui'
        })
        self.assertEquals(form.errors["tour_dates"], ['Enter a valid date.'])
    
    # Se requiere la informacion del artista
    def test_no_has_artist_info(self):
        form = FormCreateBand(data={
            'name' : 'Mi banda', 
            'tour_dates' : '2022-12-25', 
            'image' : 'Mi_imagen', 
            'artist_info' : ''
        })
        self.assertEquals(form.errors["artist_info"], ['This field is required.'])

    # Se requiere un nombre menor a 50 caracteres
    def test_more_than_hundred(self):
        textoPrueba = "Mi Banda" * 300
        form = FormCreateBand(data={
            'name' : textoPrueba, 
            'tour_dates' : '2022-12-255', 
            'image' : 'Mi_imagen', 
            'artist_info' : ''
        })
        self.assertEquals(form.errors["name"], ['Ensure this value has at most 50 characters (it has 2400).'])

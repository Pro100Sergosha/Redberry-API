from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import GeneralInfo

class GeneralInfoTests(TestCase):
            

    def setUp(self):
        self.client = APIClient()
        self.instance = GeneralInfo.objects.create(name = 'სატესტო', 
                                                      last_name = 'სატესტო', 
                                                      bio = 'სატესტო', 
                                                      email = 'testemail@redberry.ge',
                                                      number = '+995 544 44 11 39',)
        

    def test_create_general_info(self):
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('/home/sergo/Downloads/photo.jpeg', 'rb').read(),
            content_type='image/jpeg'
        )
        response = self.client.post('/api/general/', {'name': 'სერგო', 
                                                      'last_name': 'აზიზბეკიანი', 
                                                      'bio': 'აღწერა ჩემს თავზე', 
                                                      'email': 'testemail@redberry.ge',
                                                      'photo': self.test_image,
                                                      'number': '+995 544 44 11 39',
                                                      }, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.photo = GeneralInfo.objects.get(name='სერგო')
        self.photo.photo.delete()


    def test_create_errors_general_info(self):
        response = self.client.put('/api/general/1/', {'name': 'sergo'}, format='json')
        self.assertEqual(response.status_code, 400)

        # This test checks if last name is georgian
        response = self.client.put('/api/general/1/', {'last_name': 'azizbekyan'}, format='json')
        
        self.assertEqual(response.status_code, 400)

        # This test checks if bio is georgian
        response = self.client.put('/api/general/1/', {'bio': 'My New bio',}, format='json')
        
        self.assertEqual(response.status_code, 400)

        # This test checks if email ends with @redberry.ge
        response = self.client.put('/api/general/1/', {'email': 'testemail@mail.ru'}, format='json')
        
        self.assertEqual(response.status_code, 400)

        response = self.client.put('/api/general/1/', {'number': '+7 54444 11 30'})

        self.assertEqual(response.status_code, 400)
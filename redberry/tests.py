from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
class GeneralInfoTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_general_info(self):
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('path/to/your/test/image.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        response = self.client.post('/api/general/', {'name': 'სერგო', 
                                                      'last_name': 'აზიზბეკიანი', 
                                                      'bio': 'აღწერა ჩემს თავზე', 
                                                      'email': 'testemail@redberry.ge',
                                                      'photo': self.test_image,
                                                      'number': '+995 544 44 11 39',
                                                      }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_errors_general_info(self):

        # This test checks if name is georgian
        response = self.client.post('/api/general/', {'name': 'sergo', 
                                                      'last_name': 'აზიზბეკიანი', 
                                                      'bio': 'აღწერა ჩემს თავზე', 
                                                      'email': 'testemail@redberry.ge',
                                                      'number': '+995 544 44 11 39'
                                                      }, format='json')
        
        self.assertEqual(response.status_code, 400)

        # This test checks if last name is georgian
        response = self.client.post('/api/general/', {'name': 'სერგო', 
                                                      'last_name': 'azizbekyan', 
                                                      'bio': 'აღწერა ჩემს თავზე', 
                                                      'email': 'testemail@redberry.ge',
                                                      'number': '+995 544 44 11 39'
                                                      }, format='json')
        
        self.assertEqual(response.status_code, 400)

        # This test checks if bio is georgian
        response = self.client.post('/api/general/', {'name': 'სერგო', 
                                                      'last_name': 'აზიზბეკიანი', 
                                                      'bio': 'My New bio', 
                                                      'email': 'testemail@redberry.ge',
                                                      'number': '+995 544 44 11 39'
                                                      }, format='json')
        
        self.assertEqual(response.status_code, 400)

        # This test checks if email ends with @redberry.ge
        response = self.client.post('/api/general/', {'name': 'სერგო', 
                                                      'last_name': 'აზიზბეკიანი', 
                                                      'bio': 'ინფორმაცია ჩემს შესახებ', 
                                                      'email': 'testemail@mail.ru',
                                                      'number': '+995 544 44 11 39'
                                                      }, format='json')
        
        self.assertEqual(response.status_code, 400)
    
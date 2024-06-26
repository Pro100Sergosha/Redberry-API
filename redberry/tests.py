from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import GeneralInfo, ExperienceInfo, EducationInfo, Resume
import json
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

    def test_update_general_info(self):
        response = self.client.patch('/api/general/1/', {'name': 'ანზორ',
                                                         'last_name': 'მუმლაძე',
                                                         })
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'ანზორ')

    def test_delete_general_info(self):
        response = self.client.delete('/api/general/1/')
        self.assertEqual(response.status_code, 204)

    def test_check_errors_general_info(self):
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



class ExperienceInfoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.instance = ExperienceInfo.objects.create(position = 'Middle', 
                                                      employer = 'Lasha',
                                                      start_date = '2024-06-25',
                                                      end_date = '2024-07-25',
                                                      info = 'Test info')

    def test_create_experience_info(self):
        response = self.client.post('/api/experience/', {'position': 'Test Position', 
                                                         'employer': 'Sergo', 
                                                         'start_date': '2024-06-25',
                                                         'end_date': '2024-07-25',
                                                         'info': 'test info'
                                                         })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['info'], 'test info')
    
    def test_update_experience_info(self):
        response = self.client.patch('/api/experience/1/', {'position': 'Position', 
                                                            'employer': 'Dima'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['position'], 'Position')

    def test_delete_experience_info(self):
        response = self.client.delete('/api/experience/1/')
        self.assertEqual(response.status_code, 204)

class EducationInfoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.instance = EducationInfo.objects.create(education = 'Algouni', 
                                                     degree = 'სტუდენტი', 
                                                     end_date = '2024-07-01', 
                                                     info = 'test info')

    def test_create_education_info(self):
        response = self.client.post('/api/education/', {'education': 'Algosoft',
                                                        'degree': 'სტუდენტი',
                                                        'end_date': '2024-07-01',
                                                        'info': 'test info'})
        self.assertEqual(response.status_code, 201)

    def test_update_education_info(self):
        response = self.client.patch('/api/education/1/', {'degree': 'მაგისტრი'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['degree'], 'მაგისტრი')

    def test_delete_education_info(self):
        response = self.client.delete('/api/education/1/')
        self.assertEqual(response.status_code, 204)


class ResumeTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_resume(self):
        data = {
        'general': [{'id': 1,'name': 'სერგო', 'last_name': 'აზიზბეკიანი', 'bio': 'აღწერა ჩემს თავზე', 'email': 'testemail@redberry.ge', 'number': '+995 544 44 11 39'}],
        'education': [{'id': 1,'education': 'Algosoft', 'degree': 'სტუდენტი', 'end_date': '2024-07-01', 'info': 'test info'}],
        'experience': [{'id': 1,'position': 'Test Position', 'employer': 'Sergo', 'start_date': '2024-06-25', 'end_date': '2024-07-25', 'info': 'test info'}]
            }
        data = json.dumps(data)
        response = self.client.post('/api/resume/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    def test_update_delete_resume(self):
        data = {
        'general': [{'id': 1,'name': 'სერგო', 'last_name': 'აზიზბეკიანი', 'bio': 'აღწერა ჩემს თავზე', 'email': 'testemail@redberry.ge', 'number': '+995 544 44 11 39'}],
        'education': [{'id': 1,'education': 'Algosoft', 'degree': 'სტუდენტი', 'end_date': '2024-07-01', 'info': 'test info'}],
        'experience': [{'id': 1,'position': 'Test Position', 'employer': 'Sergo', 'start_date': '2024-06-25', 'end_date': '2024-07-25', 'info': 'test info'}]
            }
        data = json.dumps(data)
        response = self.client.post('/api/resume/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        data = {
        'general': [{'id': 1,'name': 'სატესტო', 'last_name': 'აზიზბეკიანი', 'bio': 'აღწერა ჩემს თავზე', 'email': 'testemail@redberry.ge', 'number': '+995 544 44 11 39'}],
        'education': [{'id': 1,'education': 'AlgoUni', 'degree': 'სტუდენტი', 'end_date': '2024-07-01', 'info': 'test info'}],
        'experience': [{'id': 1,'position': 'Junior', 'employer': 'Sergo', 'start_date': '2024-06-25', 'end_date': '2024-07-25', 'info': 'test info'}]
            }
        data = json.dumps(data)
        response = self.client.patch('/api/resume/1/', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.delete('/api/resume/1/')
        self.assertEqual(response.status_code, 204)
from django.test import TestCase,Client
from django.urls import reverse

class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
            response = self.client.get(reverse("index-page"))
            self.assertTemplateNotUsed(response,"blog/index.html") 
            self.assertEqual(500,response.status_code)

    def test_about(self):
        response = self.client.get(reverse("about-view"))
        self.assertTemplateNotUsed(response,"blog/about.html")
        self.assertEqual(500,response.status_code)

    def test_contacts(self):
        response = self.client.get(reverse("contacts-view")) 
        self.assertTemplateNotUsed(response,"blog/contacts.html")
        self.assertEqual(500,response.status_code)

    # def test_hello(self):
    #     response = self.client.get(reverse("index-page"))
    #     excepted_data = "Hello" 
    #     self.assertEqual(excepted_data,response.content.decode())  
    #     self.assertEqual(500,response.status_code)
    #     self.assertEqual(response['name'],'alex')

    # def test_about(self):
    #     response = self.client.get(reverse("about-view"))
    #     excepted_data = "white" 
    #     self.assertTemplateNotUsed(response,blog/)
    #     self.assertEqual(500,response.status_code)

    # def test_contacts(self):
    #     response = self.client.get(reverse("contacts-view"))
    #     excepted_data = "black" 
    #     self.assertEqual(excepted_data,response.content.decode())  
    #     self.assertEqual(500,response.status_code)
       

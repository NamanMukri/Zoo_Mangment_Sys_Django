from django.test import TestCase
from animals.models import Mammal, Bird, Fish
from django.urls import reverse

class AnimalTestCase(TestCase):
    def setUp(self):
        Mammal.objects.create(name='lion', species='Panthera', gender='M', food='meat')
        Bird.objects.create(name='Parrot', species='parrata', food='insects')
        Fish.objects.create(species='GoldFisha', food='grain', count=100,color='yellow')

    def test_mammal_get_query(self):
        """Animals that can speak are correctly identified"""
        lion = Mammal.objects.get(species="Panthera")
        self.assertEqual(str(lion), 'lion')
        self.assertTrue(isinstance(lion, Mammal))
    
    def test_bird_get_query(self):
        """Animals that can speak are correctly identified"""
        lion = Bird.objects.get(species="parrata")
        self.assertEqual(str(lion), 'Parrot')
        self.assertTrue(isinstance(lion, Bird))
    
    def test_fish_get_query(self):
        """Animals that can speak are correctly identified"""
        lion = Fish.objects.get(color="yellow")
        self.assertEqual(str(lion), 'GoldFisha')
        self.assertTrue(isinstance(lion, Fish))
    
    def test_mammals_get_req(self):
        url = reverse('animals:mammals')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'), '{"data": [["lion", "Panthera", "M", "meat"]]}')
        self.assertEqual(response.status_code, 200)
    
    def test_bird_get_req(self):
        url = reverse('animals:birds')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'), '{"data": [["Parrot", "parrata", "insects"]]}')
        self.assertEqual(response.status_code, 200)
    
    def test_fish_get_req(self):
        url = reverse('animals:fishes')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'), '{"data": [["yellow", "GoldFisha", "grain", 100]]}')
        self.assertEqual(response.status_code, 200)

    def test_mammals_post_req(self):
        url = reverse('animals:mammals')
        response = self.client.post(url,{'name': 'tiger','species': 'Sumatran','gender':'M','food':'chicken'})
        self.assertEqual(response.content.decode('utf-8'), '{"created": {"name": "tiger"}}')
        self.assertEqual(response.status_code, 200)
        lion = Mammal.objects.get(species="Sumatran")
        self.assertEqual(str(lion), 'tiger')
    
    def test_bird_post_req(self):
        url = reverse('animals:birds')
        response = self.client.post(url,{'name': 'crow','species': 'crowa','food':'meat'})
        self.assertEqual(response.content.decode('utf-8'), '{"created": {"name": "crow"}}')
        self.assertEqual(response.status_code, 200)
        lion = Bird.objects.get(species="crowa")
        self.assertEqual(str(lion), 'crow')
    
    def test_fish_post_req(self):
        url = reverse('animals:fishes')
        response = self.client.post(url,{'color':'brown','species': 'Tuna','food':'grains','count':2000})
        self.assertEqual(response.content.decode('utf-8'), '{"created": {"species": "Tuna"}}')
        self.assertEqual(response.status_code, 200)
        lion = Fish.objects.get(color="brown")
        self.assertEqual(str(lion), 'Tuna')
    
# new tests
    def test_mammals_delete_req(self):
        url = reverse('animals:mammals')
        response = self.client.delete(url+'lion')
        self.assertEqual(response.content.decode('utf-8'), '{"Deleted ": "lion"}')
        self.assertEqual(response.status_code, 200)
        lion = Mammal.objects.filter(species="Panthera").first()
        self.assertEqual(str(lion), 'None')
    
    def test_bird_delete_req(self):
        url = reverse('animals:birds')
        response = self.client.delete(url+'Parrot')
        self.assertEqual(response.content.decode('utf-8'), '{"Deleted ": "Parrot"}')
        self.assertEqual(response.status_code, 200)
        lion = Bird.objects.filter(species="parrata").first()
        self.assertEqual(str(lion), 'None')

    def test_fish_delete_req(self):
        url = reverse('animals:fishes')
        response = self.client.delete(url+'GoldFisha')
        self.assertEqual(response.content.decode('utf-8'), '{"Deleted ": "GoldFisha"}')
        self.assertEqual(response.status_code, 200)
        lion = Fish.objects.filter(species="GoldFisha").first()
        self.assertEqual(str(lion), 'None')

    def test_each_mammals_get_req(self):
        url = reverse('animals:mammals')
        response = self.client.get(url+'lion')
        self.assertEqual(response.content.decode('utf-8'), '{"name": "lion", "species": "Panthera", "gender": "M", "food": "meat"}')
        self.assertEqual(response.status_code, 200)
    
    def test_each_birds_get_req(self):
        url = reverse('animals:birds')
        response = self.client.get(url+'Parrot')
        self.assertEqual(response.content.decode('utf-8'), '{"name": "Parrot", "species": "parrata", "food": "insects"}')
        self.assertEqual(response.status_code, 200)
    
    def test_each_fish_get_req(self):
        url = reverse('animals:fishes')
        response = self.client.get(url+'GoldFisha')
        self.assertEqual(response.content.decode('utf-8'), '{"color": "yellow", "species": "GoldFisha", "food": "grain", "count": 100}')
        self.assertEqual(response.status_code, 200)

    def test_mammals_put_req(self):
        url = reverse('animals:mammals')
        feed_time_before = Mammal.objects.values('last_feed_time').filter(species="Panthera").first()['last_feed_time']
        response = self.client.put(url+'lion')
        feed_time_after = Mammal.objects.values('last_feed_time').filter(species="Panthera").first()['last_feed_time']
        self.assertEqual(response.content.decode('utf-8'), '{"Feeded": "lion"}')
        self.assertEqual(feed_time_before<feed_time_after, True)
    
    def test_birds_put_req(self):
        url = reverse('animals:birds')
        feed_time_before = Bird.objects.values('last_feed_time').filter(species="parrata").first()['last_feed_time']
        response = self.client.put(url+'Parrot')
        feed_time_after = Bird.objects.values('last_feed_time').filter(species="parrata").first()['last_feed_time']
        self.assertEqual(response.content.decode('utf-8'), '{"Feeded": "Parrot"}')
        self.assertEqual(feed_time_before<feed_time_after, True)
    
    def test_fish_put_req(self):
        url = reverse('animals:fishes')
        feed_time_before = Fish.objects.values('last_feed_time').filter(species="GoldFisha").first()['last_feed_time']
        response = self.client.put(url+'GoldFisha')
        feed_time_after = Fish.objects.values('last_feed_time').filter(species="GoldFisha").first()['last_feed_time']
        self.assertEqual(response.content.decode('utf-8'), '{"Feeded": "GoldFisha"}')
        self.assertEqual(feed_time_before<feed_time_after, True)



    
    


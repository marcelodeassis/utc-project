from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core import models
from core import views

import json
from pprint import pprint



class TaskUserTest(TestCase):    

    
    def setUp(self):
        self.client = APIClient()        

    
    def test_taskuser_methods(self):
        LIST_URL = reverse('core:task_users-list')        
        username = 'TEST_USER'

        # testing POST
        res_post = self.client.post(LIST_URL, {'name' : username}) 
        task_user = models.TaskUser.objects.get(**res_post.data)        
        self.assertEqual(res_post.status_code, status.HTTP_201_CREATED)        
        self.assertTrue(task_user.name == username)

        id = res_post.data['id']
        DETAIL_URL = reverse('core:task_users-detail', args=[1])

        # testing GET
        res_get = self.client.get(DETAIL_URL)
        self.assertEqual(res_get.status_code, status.HTTP_200_OK) 
        self.assertTrue(res_get.data['name'] == username)

        res_get = self.client.get(LIST_URL) 
        self.assertTrue(len(res_get.data) > 0)

        # testing PUT
        new_username = username + '_UPDATED'
        res_put = self.client.put(DETAIL_URL, {'name' : new_username})
        self.assertEqual(res_put.status_code, status.HTTP_200_OK) 
        self.assertTrue(res_put.data['name'] == new_username)

        # testing DELETE
        res_del = self.client.delete(DETAIL_URL)
        self.assertEqual(res_del.status_code, status.HTTP_204_NO_CONTENT) 

        res_get = self.client.get(LIST_URL) 
        self.assertTrue(len(res_get.data) == 0)

        res_get = self.client.get(DETAIL_URL) 
        self.assertTrue(res_get.status_code, status.HTTP_404_NOT_FOUND) 

    
    def test_taskstate_methods(self):
        LIST_URL = reverse('core:task_states-list')
        
        taskstate_name = 'WELL DONE'

        # testing POST
        res_post = self.client.post(LIST_URL, {'name' : taskstate_name}) 
        task_state = models.TaskState.objects.get(**res_post.data)        
        self.assertEqual(res_post.status_code, status.HTTP_201_CREATED)        
        self.assertTrue(task_state.name == taskstate_name)

        id = res_post.data['id']

        DETAIL_URL = reverse('core:task_states-detail', args=[id])

        # testing GET
        res_get = self.client.get(DETAIL_URL)
        self.assertEqual(res_get.status_code, status.HTTP_200_OK) 
        self.assertTrue(res_get.data['name'] == taskstate_name)

        res_get = self.client.get(LIST_URL) 
        self.assertTrue(len(res_get.data) == 3)

        # testing PUT
        new_taskstate_name = taskstate_name + '_UPDATED'
        res_put = self.client.put(DETAIL_URL, {'name' : new_taskstate_name})
        self.assertEqual(res_put.status_code, status.HTTP_200_OK) 
        self.assertTrue(res_put.data['name'] == new_taskstate_name)

        # testing DELETE
        res_del = self.client.delete(DETAIL_URL)
        self.assertEqual(res_del.status_code, status.HTTP_204_NO_CONTENT) 

        res_get = self.client.get(LIST_URL) 
        self.assertTrue(len(res_get.data) == 2)

        res_get = self.client.get(DETAIL_URL) 
        self.assertTrue(res_get.status_code, status.HTTP_404_NOT_FOUND) 
            
    
    def test_task_methods(self):
        self.assertEqual('TODO', 'TODO')
        
        


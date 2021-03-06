from django.test import TestCase,Client
from django.urls import reverse,resolve
from cv.models import Cv_section
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.cv_section_list_url=reverse('cv_section_list')
        self.cv_section_detail_url=reverse('cv_section_detail',args=[1])
        self.cv_section_new_url=reverse('cv_section_new')
        self.cv_section_edit_url=reverse('cv_section_edit',args=[1])
        self.cv_section_remove_url=reverse('cv_section_remove',args=[1])

        Cv_section.objects.create(
        title='title',
        text='my text'
        )

    def test_cv_section_list_GET(self):
        response=self.client.get(self.cv_section_list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cv/cv_sections_list.html')

    def test_uses_correct_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_sections_list.html')

    def test_cv_section_detail_GET(self):
        response=self.client.get(self.cv_section_detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cv/cv_section_detail.html')

    def test_cv_section_new_GET(self):
        response=self.client.get(self.cv_section_new_url)
        self.assertIn('title', response.content.decode())
        self.assertEquals(response.status_code,200)

    def test_cv_section_edit_GET(self):
        response=self.client.get(self.cv_section_edit_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cv/cv_section_edit.html')

    def test_cv_section_remove_GET(self):
        response=self.client.get(self.cv_section_remove_url)
        self.assertEquals(response.status_code,302)

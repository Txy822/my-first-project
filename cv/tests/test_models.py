from django.test import TestCase

from cv.models import Cv_section

class CvSectionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Cv_section.objects.create(title='title1', text='this is sample text1')
        Cv_section.objects.create(title='title1', text='this is sample text1')

    def test_title_name_label(self):
        cv_section = Cv_section.objects.get(id=1)
        title_label = cv_section._meta.get_field('title').verbose_name
        self.assertEquals(title_label, 'title')

    def test_text_name_label(self):
        cv_section = Cv_section.objects.get(id=1)
        text_label = cv_section._meta.get_field('text').verbose_name
        self.assertEquals(text_label, 'text')

    def test_title_max_length(self):
        cv_section = Cv_section.objects.get(id=1)
        max_length = cv_section._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

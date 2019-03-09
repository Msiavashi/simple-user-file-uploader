from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Template
from users.models import User

class ModelTestCase(TestCase):

    def setUp(self):
        self.owner = User(email="test@gmail.com")
        self.is_published = False
        self.template_name = "test"
        self.template = open("./serializers.py")
        self.template_model = Template(name=self.template_name, url=self.template, owner=self.owner, is_published=self.is_published)
    
    def test_model_can_create_a_template(self):
        old_count = Template.objects.count()
        self.template.save()
        new_count = Template.objects.count()
        self.assertNotEqual(old_count, new_count)

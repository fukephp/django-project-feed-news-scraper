from typing import Any, Sequence

from django.contrib.auth.models import Group, User
from faker import Faker

import factory, datetime

fake = Faker()


from ..models import Article


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Article
        
    title = fake.sentence()
    description = fake.text()
    link = fake.sentence()
    published = datetime.datetime.now()

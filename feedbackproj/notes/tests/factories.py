from datetime import date

import factory
import factory.fuzzy
from django.template.defaultfilters import slugify

from ...users.tests.factories import UserFactory
from ..models import Comment, Note


class NoteFactory(factory.django.DjangoModelFactory):
    subject = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.subject))
    forDate = factory.fuzzy.FuzzyDate(date.today())
    summary = factory.fuzzy.FuzzyText()
    details = factory.fuzzy.FuzzyText()
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Note


class CommentFactory(factory.django.DjangoModelFactory):
    note = factory.SubFactory(NoteFactory)
    creator = factory.SubFactory(UserFactory)
    body = factory.fuzzy.FuzzyText()

    class Meta:
        model = Comment

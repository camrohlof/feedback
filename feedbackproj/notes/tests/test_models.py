import pytest

from .factories import CommentFactory, NoteFactory

pytestmark = pytest.mark.django_db


def testNote__str__():
    note = NoteFactory()
    assert note.__str__() == str(note.forDate) + " - " + note.subject
    assert str(note) == str(note.forDate) + " - " + note.subject


def testComment__str__():
    comment = CommentFactory()
    assert comment.__str__() == "Comment by " + str(comment.creator)
    assert str(comment) == "Comment by " + str(comment.creator)

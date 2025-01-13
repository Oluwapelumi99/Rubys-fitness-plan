from django.contrib.auth.models import User
from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    def test_form_is_valid(self):
        """Test for the Cooment form is valid"""
        form = CommentForm({
                            'body': 'Test Form'})
        self.assertTrue(form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """Test for the Comment form is not valid, body is a required
        field and an empty string has been passed,
        that invalidates the form and the test comes back as True"""
        form = CommentForm({
                             'body': ''})
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_body_is_required(self):
        """Test for the 'body' field"""
        form = CommentForm({
            'body': '',
        })
        self.assertFalse(
            form.is_valid(),
            msg="body was not provided, but the form is valid"
        )

        
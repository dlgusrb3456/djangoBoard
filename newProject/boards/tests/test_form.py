from testcase import TestCase

from boards.forms import PostForm


class TestForms(TestCase):
    def test_post_form_valid_data(self):
        postForm = PostForm(data={'title':'title1','contents':'contents1'})
        self.assertTrue(postForm.is_valid())

    def test_post_form_valid_no_title(self):
        postForm = PostForm(data={'title': '', 'contents': 'contents1'})
        self.assertTrue(postForm.is_valid())

        self.assertFalse(postForm.is_valid())
        self.assertEqual(len(postForm.is_valid()),1)
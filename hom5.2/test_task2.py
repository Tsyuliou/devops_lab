from unittest import TestCase

import task2


class test_app(TestCase):

    def test_palindrom(self):
        self.assertTrue(task2.palindrom("adda"))
        self.assertFalse(task2.palindrom("abcd"))

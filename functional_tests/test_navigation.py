from unittest import TestCase
import kola





# our robot kola opens Linkedin web site
class NavigationTests(TestCase):
    """docstring for NavigationTests"""
    def test_can_open_browser(self):
        opened = kola.open_nav()
        self.assertTrue(opened)
        
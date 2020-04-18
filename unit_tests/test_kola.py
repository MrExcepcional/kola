from unittest import TestCase
from kola import KolaRobot
from unittest import skip


class KolaTests(TestCase):

    def setUp(self):
        self.k = KolaRobot()

    def tearDown(self):
        if self.k._working:
            self.k.close_browser()

    def test_can_read_envs(self):
        self.k._load_envs()
        self.assertIsNotNone(self.k._us)
        self.assertIsNotNone(self.k._kol)
        self.assertIsNotNone(self.k._search)

    @skip
    def test_valid_user(self):
        # ¿Is _us as email format user name?
        pass

    def test_kola_notifies_succes_open_browser(self):
        opened = self.k.open_nav()
        self.assertTrue(opened)

    def test_kola_opens_browser_with_right_url(self):
        self.k.open_nav()
        url = self.k.actual_url
        self.assertIn('linkedin.com', url)

    @skip
    def test_kola_signs_in(self):
        pass
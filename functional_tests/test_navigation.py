from unittest import TestCase, skip
from kola import KolaRobot



class NavigationTests(TestCase):
    """docstring for NavigationTests"""

    def test_kola_can_retrieve_a_job_search(self):
        # our robot kola opens Linkedin web site
        k = KolaRobot()
        k.open_nav()
        # Seeks the jobs button and clicks on it
        # Sees a job search box with id 'jobs-search-box-keyword-id-ember15'
        # Enters python in it

        # Sees another search box with id 'jobs-search-box-location-id-ember15'
        # Enters a locarion: 'Todo el mundo'

        # Waits until the page refreshes to see results of the search
        # and sees the number of results found by css selector 
        # (small.display-flex)
        self.fail('finish the test!!')

    @skip
    def test_can_scroll_through_list_of_jobs(self):
    	pass
    @skip
    def test_detects_language_of_job_description(self):
    	pass
    @skip
    def test_can_apply_a_job(self):
    	pass
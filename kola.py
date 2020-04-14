import os
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 6

def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn

class KolaRobot(object):
    """docstring for KolaRobot"""
    _working = False
    _us = None
    _kol = None
    _search = None

    def _load_envs(self):
        self._us = os.environ.get("KUSER")
        self._kol = os.environ.get("KOL")
        self._search = os.environ.get("SEARCH")

    def open_nav(self):
        self.browser = webdriver.Firefox()
        self.browser.get(
            'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        )
        _working = True
        return _working

    @wait
    def sign_in(self):
        if self.browser:
            email_box = self.browser.find_element_by_name('session_key')
            email_box.clear()
            email_box.send_keys(self._us)
            pass_box = self.browser.find_element_by_name(
                'session_password'
            )
            pass_box.clear()
            pass_box.send_keys(self._kol)
            sign_in_button = self.browser.find_element_by_class_name(
                'login__form_action_container'
            )
            sign_in_button.click()

    @wait
    def navigate_to_job_search(self):
        self.browser.find_element_by_id('jobs-tab-icon').click()

    @wait
    def fill_job_search_box(self):
        sjb = self.browser.find_element_by_id('jobs-search-box-keyword-id-ember441')
        sjb.clear()
        sjb.send_keys(self._search)

    @property
    def actual_url(self):
        return self.browser.current_url

    def close_browser(self):
        self.browser.quit()
        _working = False
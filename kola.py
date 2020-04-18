import os
import time
import pickle

from selenium import webdriver
from selenium.common.exceptions import (
    WebDriverException, 
    NoSuchElementException
)
from selenium.webdriver.common.keys import Keys


MAX_WAIT = 8
LOCATION = 'Espacio Económico Europeo'

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

    def __init__(self):
        super(KolaRobot, self).__init__()
        self._load_envs()

    def _load_envs(self):
        self._us = os.environ.get("KUSER")
        self._kol = os.environ.get("KOL")
        self._search = os.environ.get("SEARCH")

    def open_nav(self):
        self.browser = webdriver.Firefox()
        self.browser.get(
            'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        )
        # for cookie in pickle.load(open("linCookies.pkl","rb")):
        #     self.browser.add_cookie(cookie)
        self._working = True
        return self._working

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
        # Deactivate this after getting cookies
        print('Deactivate this at once (line 77 aprox).')
        pickle.dump(self.browser.get_cookies(), open("linCookies.pkl","wb"))

    @wait
    def fill_job_search_box(self):
        sjb = self.browser.find_element_by_xpath(
            "//*[starts-with(@id, 'jobs-search-box-keyword-id-ember')]")
        sjb.clear()
        sjb.send_keys(self._search)

    @wait
    def fill_job_location_box(self):
        loc = self.browser.find_element_by_xpath(
            "//*[starts-with(@id, 'jobs-search-box-location-id-ember')]")
        loc.clear()
        loc.send_keys(LOCATION)

    @wait
    def enter_search(self):
        search_button = self.browser.find_element_by_xpath(
            "//*[contains(@class,'jobs-search-box__submit-button')]"
        )
        search_button.click()

    @wait
    def get_job_search_panel(self):
        self.panel = self.browser.find_element_by_xpath(
            "//*[contains(@class,'jobs-search-results--is-two-pane')]"
        )

    def scroll_down_job_search_panel(self):
        self.panel.send_keys(Keys.PAGE_DOWN)

    # Investigate how to load all 25 results and not just the first 7
    @wait
    def get_jobs_list(self):
        jobs = self.browser.find_elements_by_css_selector(
            'time.job-card-search__time-badge')
        return jobs

    def _is_applied(self):
        try:
            self.browser.find_element_by_xpath(
                "//*[starts-with(@class, 'artdeco-inline-feedback__message')]"
            )
        except NoSuchElementException:
            return False
        return True

    def _is_there_apply_button(self):
        try:
            self.browser.find_element_by_xpath(
                "//*[starts-with(@class, 'jobs-apply-button--top-card')]"
            )
        except NoSuchElementException:
            return False
        return True

    def _exists_buena_suerte(self):
        return False
        # try:
        #     self.bonasera = self.browser.find_element_by_css_selector('li-icon.artdeco-button__icon')
        # except NoSuchElementException:
        #     return False
        # if self.bonasera.is_not_obscured():
        #   return True
        # else: return False

    def close_buena_suerte(self):
        if self._exists_buena_suerte():
            self.bonasera.click()

    @property
    def actual_url(self):
        return self.browser.current_url

    def close_browser(self):
        self.browser.quit()
        _working = False
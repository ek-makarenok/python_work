# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("https://afl-test.test.aeroflot.ru/ru-ru")
        wd.find_element_by_id("ttOri0").click()
        wd.find_element_by_id("ttOri0").clear()
        wd.find_element_by_id("ttOri0").send_keys("Санкт-Петербург, Saint Petersburg (LED), Россия, Russia")
        wd.find_element_by_id("ui-id-10").click()
        wd.find_element_by_id("ttDest0").click()
        wd.find_element_by_id("ttDest0").clear()
        wd.find_element_by_id("ttDest0").send_keys("Москва, Moscow (SVO, DME, VKO), Россия, Russia")
        wd.find_element_by_id("ui-id-20").click()
        wd.find_element_by_css_selector("span.calendarButton").click()
        wd.find_element_by_link_text("29").click()
        wd.find_element_by_link_text("8").click()
        wd.find_element_by_xpath("//label[@for='ttConfirm']").click()
        if not wd.find_element_by_id("ttConfirm").is_selected():
            wd.find_element_by_id("ttConfirm").click()
        wd.find_element_by_link_text("НАЙТИ РЕЙСЫ").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

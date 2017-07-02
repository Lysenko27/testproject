from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.base import Page
from selenium.webdriver.support.ui import WebDriverWait
import time
class ComposeMailPage(Page):
    def __init__(self, driver):
        self.from_xpath = '//div[@is="x-bubbles"]'
        self.subject_xpath = '//input[@name="subj"]'
        self.content_xpath = '//div[@role="textbox"]'
        self.send_button_xpath = '//span[@data-key="view=compose-send-link"]//span[@class="_nb-button-text"]'
        self.driver = driver

    def send_email(self, recipient, subject, content):
        self.driver.find_element_by_xpath(self.from_xpath).click()
        self.driver.find_element_by_xpath(self.from_xpath).send_keys(recipient)
        self.driver.find_element_by_xpath(self.from_xpath).click()
        self.driver.find_element_by_xpath(self.subject_xpath).send_keys(subject)
        self.driver.find_element_by_xpath(self.content_xpath).click
        self.driver.find_element_by_xpath(self.content_xpath).send_keys(content)
        self.driver.find_element_by_xpath(self.send_button_xpath).click()

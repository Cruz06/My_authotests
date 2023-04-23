import base64
import os
import time
import random

import allure
import requests
from selenium.webdriver.common.by import By
from generator.generator import *
from locators.alert_frame_window_locators import *
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators

    @allure.step('check opened new tab ')
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_PAGE).text
        return text_title

    @allure.step('check opened new window')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_TAB_PAGE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_PAGE).text
        return text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators

    @allure.step('get text from alert')
    def simple_alert_button(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('check alert appear after 5 sec')
    def alert_after_five_second(self):
        self.element_is_visible(self.locators.ALERT_AFTER_FIVE_SECOND).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('check confirm alert')
    def confirm_box(self):
        self.element_is_visible(self.locators.CONFIRM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
        text_message = self.element_is_present(self.locators.CONFIRM_BOX_ANSWER).text
        return text_message

    @allure.step('check prompt alert')
    def prompt_box(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_message = self.element_is_present(self.locators.PROMPT_BOX_ANSWER).text
        return text_message, text

class FramePage(BasePage):
    locators = FramePageLocators

    @allure.step('check frame')
    def check_frame(self, frame_number):
        if frame_number == 'frame1':
            frame = self.element_is_present(self.locators.BIG_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_PAGE).text
            self.driver.switch_to.default_content()
            return [width, height, text]
        if frame_number == 'frame2':
            frame = self.element_is_present(self.locators.SMALL_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_PAGE).text
            self.driver.switch_to.default_content()
            return [width, height, text]

class NestedFramePage(BasePage):
    locators = NestedFramePageLocators

    @allure.step('check nested frame')
    def nested_frame_page(self):
        first_frame = self.element_is_present(self.locators.FIRST_FRAME)
        self.driver.switch_to.frame(first_frame)
        text_first_frame = self.element_is_present(self.locators.FIRST_FRAME_TEXT).text
        second_frame = self.element_is_present(self.locators.SECOND_FRAME)
        self.driver.switch_to.frame(second_frame)
        text_second_frame = self.element_is_present(self.locators.SECOND_FRAME_TEXT).text
        return text_first_frame, text_second_frame

class ModalWindowPage(BasePage):
    locators = ModalWindowPageLocators

    @allure.step('check small modal dialogs')
    def small_modal_window(self):
        self.element_is_present(self.locators.SMALL_MODAL_BUTTON).click()
        small_header = self.element_is_present(self.locators.SMALL_MODAL_HEADER).text
        small_text = self.element_is_present(self.locators.SMALL_MODAL_TEXT).text
        self.element_is_visible(self.locators.SMALL_CLOSE_BUTTON).click()
        return small_header, small_text

    @allure.step('check big modal dialogs')
    def big_modal_window(self):
        self.element_is_present(self.locators.BIG_MODAL_BUTTON).click()
        big_header = self.element_is_present(self.locators.BIG_MODAL_HEADER).text
        big_text = self.element_is_present(self.locators.BIG_MODAL_TEXT).text
        self.element_is_present(self.locators.BIG_CLOSE_BUTTON).click()
        return big_header, big_text
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About

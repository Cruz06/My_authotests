import base64
import os
import time
import random

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import *
from locators.widjets_page_locators import *
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators

    @allure.step('check accordian widget')
    def check_accordian(self, accordian_number):
        accordian = {'first':
                         {'title': self.locators.FIRST_SECTION,
                          'content': self.locators.FIRST_SECTION_TEXT},
                     'second':
                         {'title': self.locators.SECOND_SECTION,
                          'content': self.locators.SECOND_SECTION_TEXT},
                     'third':
                         {'title': self.locators.THIRD_SECTION,
                          'content': self.locators.THIRD_SECTION_TEXT}
                     }
        section_title = self.element_is_visible(accordian[accordian_number]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
        return [section_title.text, section_content]

class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators

    @allure.step('fill multi autocomplete input')
    def fill_input_multi(self):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clicable(self.locators.MULTI_COLOR_NAMES)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('remove value from multi autocomplete')
    def remove_value_multi(self):
        count_value_before = len(self.elements_are_presents(self.locators.MULTI_COLOR_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_COLOR_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_presents(self.locators.MULTI_COLOR_VALUE))
        return count_value_before, count_value_after

    @allure.step('check colors in multi autocomplete')
    def check_color_in_multi(self):
        color_list = self.elements_are_presents((self.locators.MULTI_COLOR_VALUE))
        colors = []
        for i in color_list:
            colors.append(i.text)
        return colors

    @allure.step('fill single autocomplete input')
    def fill_single_auto_complete(self):
        color = random.sample(next(generator_color()).color_name, k=1)
        input_color = self.element_is_visible(self.locators.SINGLE_COLOR_INPUT)
        input_color.send_keys(color)
        input_color.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('check color in single autocomplete')
    def check_single_color(self):
        color = self.element_is_visible(self.locators.SINGLE_COLOR_NAME)
        return color.text

    @allure.step('remove all values')
    def remove_all_value(self):
        empty_input = self.element_is_visible(self.locators.REMOVE_ALL_VALUE).click()
        return empty_input

class DatePickerPage(BasePage):
    locators = DatePickerPageLocators

    @allure.step('change date')
    def select_date(self):
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('select date by text')
    def set_date_by_text(self, elem, value):
        select = Select(self.element_is_clicable(elem))
        select.select_by_visible_text(value)

    @allure.step('select date item from list')
    def set_date_item_from_list(self, elem, value):
        item_list = self.elements_are_presents(elem)
        for i in item_list:
            if i.text == value:
                i.click()
                break

    @allure.step('change select date and time')
    def select_date_and_time(self):
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clicable(self.locators.DATE_AND_TIME_MONTH).click()
        time.sleep(2)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        time.sleep(2)
        self.element_is_clicable(self.locators.DATE_AND_TIME_YEAR).click()
        time.sleep(2)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, date.year)

        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible((self.locators.DATE_AND_TIME_INPUT))
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators

    @allure.step('change slider value')
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBar(BasePage):
    locators = ProgressBarLocators

    @allure.step('change progress bar value')
    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        button = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
        button.click()
        time.sleep((random.randint(2, 7)))
        button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators

    @allure.step('check tabs')
    def check_tabs(self, tabs_name):
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                     'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title':self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT}
                }
        button = self.element_is_visible(tabs[tabs_name]['title'])
        button.click()
        content = self.element_is_visible((tabs[tabs_name]['content'])).text
        return [button.text, len(content)]

class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators

    @allure.step('get text from tool tip')
    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    @allure.step('check tool tip')
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        time.sleep(0.5)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        time.sleep(0.5)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY)
        time.sleep(0.5)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section

class MenuPage(BasePage):
    locators = MenuPageLocators

    @allure.step('check menu item')
    def check_menu(self):
        menu_item_list = self.elements_are_presents(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            time.sleep(0.5)
            self.action_move_to_element(item)
            data.append(item.text)
        return data
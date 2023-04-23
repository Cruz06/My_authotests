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
from locators.interactions_locators import *
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators

    @allure.step('get sortable items')
    def get_sortable_items(self, elem):
        item_list = self.elements_are_visible(elem)
        return [item.text for item in item_list]

    @allure.step('change list order')
    def change_list(self):
        self.element_is_visible(self.locators.LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=3)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    @allure.step('change grade order')
    def change_grid(self):
        self.element_is_visible(self.locators.GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=3)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after

class SelectablePage(BasePage):
    locators = SelectablePageLocators

    @allure.step('click selectable item')
    def click_selected_item(self, elem):
        item_list = self.elements_are_visible(elem)
        random.sample(item_list, k=1)[0].click()

    @allure.step('select list item')
    def select_list_item(self):
        self.element_is_visible(self.locators.LIST).click()
        self.click_selected_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    @allure.step('select grid item')
    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID).click()
        self.click_selected_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text

class ResizablePage(BasePage):
    locators = ResizablePageLocators

    @allure.step('get px from width and height')
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('get max and min size')
    def get_max_and_min_size(self, elem):
        size = self.element_is_present(elem)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('change size resizable box')
    def change_size_resaziable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -200)
        min_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('change size resizable')
    def change_size_resaziable(self):
        qw = self.element_is_present(self.locators.RESIZABLE_HANDLE)
        self.go_to_element(qw)
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 500), random.randint(1, 500))
        max_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-500, -1), random.randint(-500, -1))
        min_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE))
        return max_size, min_size

class DroppablePage(BasePage):
    locators = DroppablePageLocators

    @allure.step('drop simple div')
    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('drop accept div')
    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_not_acceptable = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_acceptable = drop_div.text
        return drop_acceptable, drop_not_acceptable

    @allure.step('drop prevent propogation div')
    def drop_prevent(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box,text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    @allure.step('drop will reventable')
    def drop_will_revertable(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_div = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        position_before = drag_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_div.get_attribute('style')
        return position_before, position_after

    @allure.step('drop will not reventable')
    def drop_not_revertable(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_div = self.element_is_visible(self.locators.NOT_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        position_before = drag_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_div.get_attribute('style')
        return position_before, position_after

class DragablePage(BasePage):
    locators = DragablePageLocators

    @allure.step('get before and after positions')
    def simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_before = self.element_is_visible(self.locators.SIMPLE_DRAG)
        position_before = drag_before.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_before, random.randint(1, 300), random.randint(1, 300))
        drag_after = self.element_is_visible(self.locators.SIMPLE_DRAG)
        position_after = drag_after.get_attribute('style')
        return position_before, position_after

    @allure.step('drag only_y')
    def axis_y_restricted(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        drag_y_before = self.element_is_visible(self.locators.ONLY_Y)
        position_y_before = drag_y_before.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_y_before, 0, random.randint(1, 300))
        drag_y_after = self.element_is_visible(self.locators.ONLY_Y)
        position_y_after = drag_y_after.get_attribute('style')
        return position_y_before, position_y_after

    @allure.step('drag only_x')
    def axis_x_restricted(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        drag_x_before = self.element_is_visible(self.locators.ONLY_X)
        position_x_before = drag_x_before.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_x_before, random.randint(1, 300), 0)
        drag_x_after = self.element_is_visible(self.locators.ONLY_X)
        position_x_after = drag_x_after.get_attribute('style')
        return position_x_before, position_x_after
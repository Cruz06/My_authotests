import time

import allure

from pages.interactions_page import *

@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('Sortable Page')
    class TestSortablePage:
        @allure.title('Check changed sortable list and grid')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before_list, after_list = sortable_page.change_list()
            before_grid, after_grid = sortable_page.change_grid()
            assert before_list != after_list
            assert before_grid != after_grid

    @allure.feature('Selectable Page')
    class TestSelectablePage:
        @allure.title('Check changed selectable list and grid')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            list_item = selectable_page.select_list_item()
            grid_item = selectable_page.select_grid_item()
            assert len(list_item) > 0
            assert len(grid_item) > 0

    @allure.feature('Resizable Page')
    class TestResizable:
        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            min_box, max_box = resizable_page.change_size_resaziable_box()
            min_page, max_page = resizable_page.change_size_resaziable()
            assert min_box != max_box
            assert min_page != max_page

    @allure.feature('Droppable Page')
    class TestDroppable:
        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            simple_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            simple_droppable_page.open()
            text = simple_droppable_page.drop_simple()
            assert text == "Dropped!"

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            accept_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            accept_droppable_page.open()
            accept, not_accept = accept_droppable_page.drop_accept()
            assert accept == "Dropped!"
            assert not_accept != "Dropped!"

        @allure.title('Check prevent propogation droppable')
        def test_prevent_droppable(self, driver):
            prevent_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            prevent_droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = prevent_droppable_page.drop_prevent()
            assert not_greedy == "Dropped!"
            assert not_greedy_inner == "Dropped!"
            assert greedy == "Outer droppable"
            assert greedy_inner == "Dropped!"

        @allure.title('Check revert draggable droppable')
        def test_revert_droppable(self, driver):
            revert_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_will_revertable()
            assert before != after

        @allure.title('Check not_revert draggable droppable')
        def test_not_revert_droppable(self, driver):
            revert_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_not_revertable()
            assert before == after

    @allure.feature('Draggable Page')
    class TestDragable:
        @allure.title('Check simple draggable')
        def test_simple_dragable_page(self, driver):
            drag_able_page = DragablePage(driver, "https://demoqa.com/dragabble")
            drag_able_page.open()
            before, after = drag_able_page.simple()
            assert before != after

        @allure.title('Check axis restricted draggable y_page')
        def test_axis_restricted_y_page(self, driver):
            drag_able_page = DragablePage(driver, "https://demoqa.com/dragabble")
            drag_able_page.open()
            before_y, after_y = drag_able_page.axis_y_restricted()
            assert before_y != after_y

        @allure.title('Check axis restricted draggable x_page')
        def test_axis_restricted_x_page(self, driver):
            drag_able_page = DragablePage(driver, "https://demoqa.com/dragabble")
            drag_able_page.open()
            before_x, after_x = drag_able_page.axis_x_restricted()
            assert before_x != after_x
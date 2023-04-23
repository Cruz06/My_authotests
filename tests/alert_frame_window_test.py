import time
import allure
from pages.alert_frame_window_page import *


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindow:
        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new tab is not find"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            text_result = new_window_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new window is not find"

    @allure.feature('Alerts Page')
    class TestAlertsPage:
        @allure.title('Checking the opening of an alert')
        def test_simple_alert(self, driver):
            simple_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            simple_alert.open()
            alert_text = simple_alert.simple_alert_button()
            assert alert_text == 'You clicked a button'

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_after_five_second(self, driver):
            alert_after_five_second = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_after_five_second.open()
            alert_text = alert_after_five_second.alert_after_five_second()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_box(self, driver):
            comfirm_box_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            comfirm_box_alert.open()
            text_message = comfirm_box_alert.confirm_box()
            assert text_message == "You selected Cancel"

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_box(self, driver):
            prompt_box_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            prompt_box_alert.open()
            text_message, text = prompt_box_alert.prompt_box()
            assert text_message == f"You entered {text}"

    @allure.feature('Frame Page')
    class TestFramePage:
        @allure.title('Check the page with frames')
        def test_frame(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result1 = frame_page.check_frame('frame1')
            result2 = frame_page.check_frame('frame2')
            assert result1 == ['500px', '350px', 'This is a sample page'], "The frame does not exest"
            assert result2 == ['100px', '100px', 'This is a sample page'], "The frame does not exest"

    @allure.feature('Nested Page')
    class TestNestedFrame:
        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            text_first_frame, text_second_frame = nested_frame_page.nested_frame_page()
            assert text_first_frame == "Parent frame", "The parent frame does not exist"
            assert text_second_frame == "Child Iframe", "The child frame does not exist"

    @allure.feature('Modal Dialog Page')
    class TestModalWindow:
        @allure.title('Check the page with small modal dialogs')
        def test_small_modal_window(self, driver):
            modal_window_page = ModalWindowPage(driver, "https://demoqa.com/modal-dialogs")
            modal_window_page.open()
            header_small_modal_window, text_small_modal_window = modal_window_page.small_modal_window()
            assert header_small_modal_window == "Small Modal", "Title in small modal window does not found"
            assert text_small_modal_window == "This is a small modal. It has very less content", "Text in small modal window does not found"

        @allure.title('Check the page with big modal dialogs')
        def test_big_modal_window(self, driver):
            modal_window_page = ModalWindowPage(driver, "https://demoqa.com/modal-dialogs")
            modal_window_page.open()
            header_big_modal_window, text_big_modal_window = modal_window_page.big_modal_window()
            assert header_big_modal_window == "Large Modal", "Title in big modal window does not found"
            assert "Lorem Ipsum is simply dummy text of the printing and typesetting industry." in text_big_modal_window, "Text in big modal window does not found"
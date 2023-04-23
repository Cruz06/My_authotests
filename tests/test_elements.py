import time

import allure

from pages.elements_page import *

@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            time.sleep(5)
            assert full_name == output_name, "The full name does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_current_address, "The current address does not mat"
            assert permanent_address == output_permanent_address, "The permanent address does not match"
    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    @allure.feature("RadioButton")
    class TestRadioButton:
        @allure.title("Check Radio Button")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "YES have not been selected"
            assert output_impressive == 'Impressive', "IMPRESSIVE have not been selected"
            assert output_no == 'No', "NO have not been selected"

    @allure.feature("WebTable")
    class TestWebTable:
        @allure.title('Сheck to add a person to the table')
        def test_add_person_in_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            return_result = web_table_page.check_new_added_person()
            assert new_person in return_result

        @allure.title('Check human search in table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_people(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "The person was not found in the table"

        @allure.title('Checking to update the persons info in the table')
        def test_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_people(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "The person card has not been changed"

        @allure.title('Checking to remove a person from the table')
        def test_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_people(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found", "The person card has not been changed"

        @allure.title('Check the change in the number of rows in the table')
        def test_web_table_change_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or has changed incorrectly'

    @allure.feature("Buttons Page")
    class TestButtonPage:
        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

    @allure.feature("Links Page")
    class TestLinksPage:
        @allure.title('Checking the link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title('Checking the broken link')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "The link works or the status code in son 400"

    @allure.feature("Upload and Download page")
    class TestDowmloadAndUploadPage:
        @allure.title('Check upload file')
        def test_upload_file(self, driver):
            upload_page = UploadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert file_name == result, "The has not been upload"

        @allure.title('Check download file')
        def test_download_file(self, driver):
            download_page = DownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True, "The file is not been download"

    @allure.feature('Dynamic properties page')
    class TestDynamicButtons:
        @allure.title('Check enable button')
        def test_enable_button(self, driver):
            enable_button = DynamicPage(driver, 'https://demoqa.com/dynamic-properties')
            enable_button.open()
            clickable = enable_button.check_enable_button()
            assert clickable is True, "The button is not been clickable after 5 second"

        @allure.title('Check dynamic properties')
        def test_dynamic_properties(self, driver):
            dynamic_buttons_page = DynamicPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_buttons_page.open()
            before_color, after_color = dynamic_buttons_page.check_changed_of_color()
            assert before_color != after_color and after_color == "rgba(220, 53, 69, 1)", "The colors have not benn changed"

        @allure.title('Check appear button')
        def test_appear_button(self, driver):
            appear_buttons_page = DynamicPage(driver, 'https://demoqa.com/dynamic-properties')
            appear_buttons_page.open()
            appear = appear_buttons_page.check_appear_button()
            assert appear is True, "The button is not appear after 5 second"
import allure

from pages.widjets_page import *

@allure.suite('Widgets')
class TestWidjets:
    @allure.feature('Accordian Page')
    class TestAccordianPage:
        @allure.title('Check accordian widget')
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian(accordian_choice())
            assert title == "What is Lorem Ipsum?" or title == "Where does it come from?" or title == "Why do we use it?"
            assert len(content) > 0

    @allure.feature('Autocomplete page')
    class TestAutoComplete:
        @allure.title('Check the autocomplete is filled')
        def test_multi_auto_complete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result

        @allure.title('Check deletions from the multi autocomplete')
        def test_remove_auto_complete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            color_before, color_after = autocomplete_page.remove_value_multi()
            assert color_before != color_after

        @allure.title('Remove all colors')
        def test_remove_all_colors(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = len(autocomplete_page.fill_input_multi())
            empty_input = autocomplete_page.remove_all_value()
            assert colors != 0
            assert empty_input is None

        @allure.title('Simple color')
        def test_simple_color(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_single_auto_complete()
            check_color = autocomplete_page.check_single_color()
            assert color in check_color

    @allure.feature('Date Picker Page')
    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after

        @allure.title('Check change date and time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after

    @allure.feature('Slider Page')
    class TestSlider:
        @allure.title('Check moved slider')
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after

    @allure.feature('Progress Bar Page')
    class TestProgressBar:
        @allure.title('Check changed progress bar')
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBar(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            before, after = progress_bar_page.change_progress_bar_value()
            assert before != after

    @allure.feature('Test Tabs Page')
    class TestTabsPage:
        @allure.title('Check switched tabs')
        def test_tabs_page(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            what_content = tabs_page.check_tabs('what')
            origin_content = tabs_page.check_tabs('origin')
            use_content = tabs_page.check_tabs('use')
            more_content = tabs_page.check_tabs('more')
            assert what_content[0] == 'What' and what_content[1] != 0, "The tab 'what' was not pressed or text is missing"
            assert origin_content[0] == 'Origin' and origin_content[1] != 0, "The tab 'origin' was not pressed or text is missing"
            assert use_content[0] == 'Use' and use_content[1] != 0, "The tab 'use' was not pressed or text is missing"
            assert more_content[0] == 'More' and more_content[1] != 0, "The tab 'more' was not pressed or text is missing"

    @allure.feature('Tool Tips')
    class TestToolTipsPage:
        @allure.title('Check tool tips ')
        def test_tool_tips_page(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
            assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    @allure.feature('Menu Page')
    class TestMenuPage:
        @allure.title('Check all of the menu items')
        def test_menu_page(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
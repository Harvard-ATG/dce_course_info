from selenium.webdriver.common.by import By

from selenium_tests.base_page import BasePage

from selenium.common.exceptions import NoSuchElementException

class EditorPageLocators(object):
    # locators for main editor page
    NEW_PAGE_SUBMIT = (By.ID, 'new_page_submit')
    TOOL_BUTTON = (By.CSS_SELECTOR,
                   'div[aria-label="Import Course Info - dev (root account)"] button')

    # locators for course info tool iframe
    # DESCRIPTION_CHECKBOX = (By.ID, 'description')
    # EXAM_GROUP_CHECKBOX = (By.ID, 'exam_group')
    # INSTRUCTORS_CHECKBOX = (By.ID, 'instructors_display')
    # LOCATION_CHECKBOX = (By.ID, 'location')
    # MEETING_TIME_CHECKBOX = (By.ID, 'meeting_time')
    # NOTES_CHECKBOX = (By.ID, 'notes')
    # REGISTRAR_CODE_CHECKBOX = (By.ID, 'course.registrar_code_display')
    # TERM_CHECKBOX = (By.ID, 'term.display_name')
    # TITLE_CHECKBOX = (By.ID, 'title')
    # TOOL_SUBMIT_BUTTON = (By.ID, 'iframe_submit')


class EditorPage(BasePage):
    locator_class = EditorPageLocators
    located_properties = [
        # 'description_checkbox',
        # 'exam_group_checkbox',
        'new_page_submit',
        # 'instructors_checkbox',
        # 'location_checkbox',
        # 'meeting_time_checkbox',
        # 'notes_checkbox',
        # 'registrar_code_checkbox',
        # 'term_checkbox',
        # 'title_checkbox',
        # 'tool_button',
        # 'tool_submit_button',
    ]
    tool_frame_name = 'external_tool_button_frame'

    def open_tool(self):
        self.tool_button.click()
        self.focus_on_tool_frame()

    def is_loaded(self):
        """ determine if the page loaded by looking for a specific element on the page """
        try:
            self.find_element(*EditorPageLocators.NEW_PAGE_SUBMIT)
        except NoSuchElementException:
            return False
        return True


from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_TAB_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")

class AlertsPageLocators:
    SIMPLE_ALERT = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_BOX_ANSWER = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_BOX = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_BOX_ANSWER = (By.CSS_SELECTOR, "span[id='promptResult']")

class FramePageLocators:
    BIG_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SMALL_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAME_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class NestedFramePageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FIRST_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    SECOND_FRAME_TEXT = (By.CSS_SELECTOR, "p")

class ModalWindowPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    SMALL_MODAL_HEADER = (By.CSS_SELECTOR, "div[class='modal-title h4']")
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, "div[class='modal-body']")
    SMALL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")

    BIG_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    BIG_MODAL_HEADER = (By.CSS_SELECTOR, "div[class='modal-title h4']")
    BIG_MODAL_TEXT = (By.CSS_SELECTOR, "div[class='modal-body']")
    BIG_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT=10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_for_load_element(self, locator, timeout=None):
        if timeout is None:
            timeout = TIMEOUT
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_clickable_element(self, locator):
        WebDriverWait(self.driver, TIMEOUT).until(expected_conditions.element_to_be_clickable(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    def input_to_element(self, locator, data):
        return self.driver.find_element(*locator).send_keys(data)

    def move_mouse_to_element(self, element):
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    def scroll_to_element(self, locator):
        element=self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)


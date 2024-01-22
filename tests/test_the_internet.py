from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

URL = "https://the-internet.herokuapp.com/"


class TestClassTheInternetSite:

    def setup_method(self):
        self.driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.var = {}

    def teardown_method(self):
        self.driver.quit()

    def test_open_url(self):
        self.driver.get(URL)
        assert self.driver.title == "The Internet"

    def test_drag_and_drop(self):
        self.driver.get(URL)
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/drag_and_drop"]').click()
        assert self.driver.find_element(By.XPATH, '//h3[normalize-space()="Drag and Drop"]').text == "Drag and Drop"

        element_a = self.driver.find_element(By.ID, "column-a")
        element_b = self.driver.find_element(By.ID, "column-b")

        action = ActionChains(self.driver)
        action.drag_and_drop(element_a, element_b).perform()

        assert element_a.text == "B"
        assert element_b.text == "A"



import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBaidu():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def switch_new(self):
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    def test_selenium(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.LINK_TEXT,"新闻").click()
        #点击过“新闻”之后，打开了新的tab页，所以需要获取新的页面权柄，并切换到相关tab页
        self.switch_new()
        self.driver.find_element(By.LINK_TEXT,"网页").click()
        self.switch_new()
        #检查某元素是否可以点击，等待时间10s，使用场景：若某元素可点击，再进行下一步操作
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="hot-title"]')))
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@class="hot-title"]')))


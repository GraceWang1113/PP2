import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

"""
基本用法：
1、生成一个动作action=ActionChains(driver)
2、动作添加方法1 action.方法1
3、动作添加方法2 action.方法2
4、调用perform()方法执行（action.perform()）
"""
class TestAction:
    def setup_method(self):
        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def switch_new(self):
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    def test_click_actions(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("lulu")
        self.driver.find_element(By.CSS_SELECTOR,"#su").click()

        element_click = self.driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/h3/a')
        element_double_click = self.driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/div[2]/div[1]/span')
        element_right_click = self.driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/div[2]/div[1]')
        action = ActionChains(self.driver)
        action.double_click(element_double_click)
        action.context_click(element_right_click)
        action.click(element_click)
        time.sleep(3)
        action.perform()
        time.sleep(3)

    def test_move_actions(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID,"s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(5)

    def test_drag_drop_action(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element(By.ID,"dragger")
        ele_drop = self.driver.find_element(By.XPATH,'/html/body/div[4]')

        action = ActionChains(self.driver)
        #action.drag_and_drop(ele_drag,ele_drop)
        #相同的操作还可以这样写
        #action.click_and_hold(ele_drag).release(ele_drop)
        #相同的操作还可以这样写
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release()
        action.perform()
        time.sleep(5)


    def test_keys_actions(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        element = self.driver.find_element(By.XPATH,"/html/body/label[1]/input")
        element.click()

        actions = ActionChains(self.driver)
        actions.send_keys("username").pause(1)
        actions.send_keys(Keys.SPACE).pause(1)
        actions.send_keys("tom").pause(1)
        actions.send_keys(Keys.BACKSPACE).pause(1)
        actions.perform()

    def test_touch_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        # op = webdriver.ChromeOptions()
        # op.add_experimental_option("w3c",False)
        # self.driver = webdriver.Chrome(options=op)

        ele_sendkeys = self.driver.find_element(By.ID,"kw")
        ele_sendkeys.send_keys("selenium测试")
        ele_search = self.driver.find_element(By.ID,"su")
        ele_search.click()
        #scroll_origin = ScrollOrigin.from_element(ele_search)
        scroll_origin = ScrollOrigin.from_viewport(0,0)
        print(type(scroll_origin))
        time.sleep(5)

        actions = ActionChains(self.driver)
        # actions.scroll_by_amount(0,10000)
        actions.scroll_from_origin(scroll_origin,0,10000)
        actions.perform()
        time.sleep(3)





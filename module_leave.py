import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class TC_Leave(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        # precondition: user login
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        browser.find_element(By.XPATH,"//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(5)

    def test_a_success_apply_leave(self):
        # step to apply leave
        browser = self.browser
        browser.implicitly_wait(3)
        browser.find_element(By.LINK_TEXT, "Leave").click()
        browser.find_element(By.LINK_TEXT, "Apply").click()
        time.sleep(3)
        dropdown = "//form[@class='oxd-form']/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']"
        browser.find_element(By.XPATH, dropdown).click()
        browser.find_element(By.XPATH, "//span[text()='CAN - Bereavement']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[1]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").send_keys("2022-12-30")
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']//button[@type='submit']").submit()
        time.sleep(5)
        # assert response message
        try:
            wait = WebDriverWait(browser, 10)
            response_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[1]"))).text
            response_message_desc = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]"))).text
            self.assertEqual(response_message, 'Success')
            self.assertIn('Successfully Saved', response_message_desc)
        except:
            assert False

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()

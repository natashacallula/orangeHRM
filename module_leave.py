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
        browser.implicitly_wait(2)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        # precondition: user login
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        browser.find_element(By.XPATH,"//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(5)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()

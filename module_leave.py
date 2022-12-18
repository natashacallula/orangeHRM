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

    def test_b_failed_apply_leave(self):
        # step to apply leave
        browser = self.browser
        browser.implicitly_wait(3)
        browser.find_element(By.LINK_TEXT, "Leave").click()
        browser.find_element(By.LINK_TEXT, "Apply").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(5)
        # assert error message
        leave_type_err_message = browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[1]//span[.='Required']").text
        from_date_err_message = browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[1]/div/span[.='Required']").text
        to_date_err_message = browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[2]/div/span[.='Required']").text
        self.assertEqual(leave_type_err_message, 'Required')
        self.assertEqual(from_date_err_message, 'Required')
        self.assertEqual(to_date_err_message, 'Required')

    def test_c_success_search_my_leave(self):
        # step to assign leave
        browser = self.browser
        browser.implicitly_wait(3)
        browser.find_element(By.LINK_TEXT, "Leave").click()
        browser.find_element(By.LINK_TEXT, "My Leave").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[@class='oxd-form-row']//div[.='Clear']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").send_keys("2022-12-30")
        time.sleep(3)
        browser.find_element(By.XPATH, " //form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[@class='oxd-form-row']//div[.='Clear']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").send_keys("2022-12-30")
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").click()
        browser.find_element(By.XPATH, "//span[text()='CAN - Bereavement']").click()
        browser.find_element(By.XPATH, "//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(5)
        # assert response message
        response_message_date = browser.find_element(
            By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div").text
        response_message_type = browser.find_element(
            By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div").text
        self.assertIn('2022-12-30', response_message_date)
        self.assertEqual(response_message_type, 'CAN - Bereavement')

    def test_d_failed_assign_leave(self):
        # step to assign leave
        browser = self.browser
        browser.implicitly_wait(3)
        browser.find_element(By.LINK_TEXT, "Leave").click()
        browser.find_element(By.LINK_TEXT, "Assign Leave").click()
        time.sleep(5)
        browser.find_element(By.XPATH, "//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("C")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div[2]/div[1]").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[1]/div//div[@class='oxd-select-wrapper']/div").click()
        browser.find_element(By.XPATH, "//span[text()='CAN - Bereavement']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[3]/div/div[1]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").send_keys("2022-12-31")
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").submit()
        time.sleep(5)
        try:
            wait = WebDriverWait(browser, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]"))).click()      
        except:
            pass
        # assert response message
        try:
            wait = WebDriverWait(browser, 15)
            response_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[1]"))).text
            response_message_desc = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]"))).text
            self.assertEqual(response_message, 'Error')
            self.assertIn('No Working Days Selected', response_message_desc)
        except:
            assert False

    def test_h_success_assign_leave(self):
        # step to assign leave
        browser = self.browser
        browser.implicitly_wait(3)
        browser.find_element(By.LINK_TEXT, "Leave").click()
        browser.find_element(By.LINK_TEXT, "Assign Leave").click()
        time.sleep(5)
        browser.find_element(By.XPATH, "//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("R")
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div[2]/div[1]").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[2]/div/div[1]/div//div[@class='oxd-select-wrapper']/div").click()
        browser.find_element(By.XPATH, "//span[text()='CAN - FMLA']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[3]/div/div[1]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").send_keys("2022-12-30")
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input[@placeholder='yyyy-mm-dd']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[4]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        browser.find_element(By.XPATH, "//span[text()='Specify Time']").click()
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[4]/div/div[2]/div/div[2]/div[@class='oxd-time-wrapper']/div[@class='oxd-time-input']/input[@placeholder='hh:mm']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[4]/div//div[@role='alert']/div[@class='oxd-time-hour-input']/i[1]").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[4]/div//div[@role='alert']/div[@class='oxd-time-hour-input']/i[1]").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[4]/div/div[2]/div/div[2]/div[@class='oxd-time-wrapper']/div[@class='oxd-time-input']/input[@placeholder='hh:mm']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//textarea").send_keys("Check up to doctor")
        time.sleep(3)
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[@class='oxd-form-actions']").submit()
        time.sleep(5)
        try:
            wait = WebDriverWait(browser, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]"))).click()      
        except:
            pass
        # assert response message
        try:
            wait = WebDriverWait(browser, 15)
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

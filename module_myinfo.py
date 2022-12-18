import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TC_MyInfo(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") #input username
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") #input password
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click() #click submit button
        time.sleep(3)

    def test_a_editPersonalInfo(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewMyDetails']/span[.='My Info']").click() #click myinfo menu
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").send_keys(Keys.DELETE)# delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']").send_keys("Luis") # change first name
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[1]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']").send_keys("Bond") # change middle name
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[2]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[2]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[1]/div[2]/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input").send_keys("Anya") # change Nickname
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[2]/div[2]/div[1]/div//input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[2]/div[2]/div[1]/div//input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[2]/div[2]/div[1]/div//input").send_keys("1234567890123") # change Driver's License Number
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[2]/div[2]/div[2]/div//i").click() # change License Expiry Date
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[2]/div[2]/div[2]/div//input[@placeholder='yyyy-mm-dd']").send_keys("2023-12-11")
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[4]/div/div[1]/div//input").send_keys(Keys.CONTROL + "a") # change Military Service
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[4]/div/div[1]/div//input").send_keys(Keys.DELETE)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[4]/div/div[1]/div//input").send_keys("testing military service")
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)
        response_message = browser.find_element(By.XPATH, "//p[@data-v-89ccd62c]").text
        self.assertIn('Success', response_message)
        time.sleep(5)
    
    def test_b_editContactDetails(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewMyDetails']/span[.='My Info']").click() #click myinfo menu
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@role='tablist']/div[2]/a[@href='/web/index.php/pim/contactDetails/empNumber/7']").click() #click contact details
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[1]/div/div[2]/input").send_keys("Pahlawan") #input Street 1
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[2]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[2]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[2]/div/div[2]/input").send_keys("Revolusi") #input Street 2
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[3]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[3]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[3]/div/div[2]/input").send_keys("DKI Jakarta") #input city
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[4]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[4]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[4]/div/div[2]/input").send_keys("DKI Jakarta") #input State / Province
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[5]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[5]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[5]/div/div[2]/input").send_keys("13430") #input Zip Portal
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div//i").click() #select Country
        browser.find_element(By.XPATH, "//span[@data-v-15ec1d6f]").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[1]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[1]/div/div[2]/input").send_keys("123456789001") #input Telephone Home
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[2]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[2]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[2]/div/div[2]/input").send_keys("100987654321") #input Telephone mobile
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[3]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[3]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[3]/div/div[2]/input").send_keys("098765432112") #input Telephone Work
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # select all text inside textfield
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/input").send_keys(Keys.DELETE) # delete text
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/input").send_keys("laul01@mail.com") #input Other Email
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(1)
        response_message = browser.find_element(By.XPATH, "//p[@data-v-89ccd62c]").text
        self.assertIn('Success', response_message)
        time.sleep(5)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TC_Admin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") #input username
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") #input password
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click() #click submit button

    def test_a_searchUser(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #click admin menu
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/input").send_keys("")
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]//i").click()
        browser.find_element(By.XPATH, "//span[@data-v-15ec1d6f]").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("p")
        browser.find_element(By.XPATH, "//span[@data-v-30f0a592]").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]//i").click()
        browser.find_element(By.XPATH, "//span[@data-v-15ec1d6f]").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(5)
        response_message = browser.find_element(By.XPATH, "//div[@data-v-0dea79bd]").text
        self.assertIn('(1) Record Found', response_message)

    def test_b_addUser(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #click admin menu
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]//i").click()
        browser.find_element(By.XPATH, "//span[@data-v-15ec1d6f]").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div/div[2]/div[@class='oxd-select-wrapper']/div//i").click()
        browser.find_element(By.XPATH, "//span[@data-v-15ec1d6f]").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("p")
        time.sleep(3)
        browser.find_element(By.XPATH, "//span[@data-v-30f0a592]").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/input").send_keys("Paul123") #input users
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']").send_keys("Paul123!") #input  password
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']").send_keys("Paul123!") #input confirm password
        time.sleep(5)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]").click() #save button
        response_message = browser.find_element(By.XPATH, "//p[@data-v-89ccd62c]").text
        self.assertIn('Success', response_message)

    def test_c_deleteUser(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click( #click admin menu
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[5]/div[@role='row']/div[1]//i").click() #click row user
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='button']").click() #click delete selected 
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]").click() # confirmation delete
        response_message = browser.find_element(By.XPATH, "//p[@data-v-89ccd62c]").text
        self.assertIn('Success', response_message)
        time.sleep(5)

    def test_d_editUser(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #click admin menu
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[2]/div[@role='row']/div[6]/div/button[2]/i").click() #click Edit icon
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # change username
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/input").send_keys(Keys.DELETE)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/input").send_keys("Carolina")
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]//i").click() #click yes, change password
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']").send_keys("Paul123!") #change pass
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']").send_keys("Paul123!") # change confirm pass
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click() # click save
        response_message = browser.find_element(By.XPATH, "//p[@data-v-89ccd62c]").text
        self.assertIn('Success', response_message)
        time.sleep(5)

    def test_e_deleteMultipleUsers(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #click admin menu
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[4]/div[@role='row']/div[1]//i").click() #select users
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[5]/div[@role='row']/div[1]//i").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[6]/div[@role='row']/div[1]//i").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[7]/div[@role='row']/div[1]//i").click() 
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='button']").click() #click delete selected
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]").click() #confirmation delete
        response_message = browser.find_element(By.XPATH, "//p[@data-v-89ccd62c]").text
        self.assertIn('Success', response_message)
        time.sleep(5)

    Admin menu -> Nationalities
    def test_f_addNationalities(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #click admin menu
        browser.find_element(By.XPATH, "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[5]/a[@href='#']").click() #click nationalities menu
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/div/button[@type='button']").click() #click add button
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//input").send_keys("Indonesia Satu")
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)
        response_message = browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//span[@class='oxd-text oxd-text--span']").text
        self.assertIn('Records Found', response_message)
        time.sleep(5)


    def test_g_deleteNationalities(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #click admin menu
        browser.find_element(By.XPATH, "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[5]/a[@href='#']").click() #click nationalities menu
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[1]//i").click() #select nationalities
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='button']").click() # delete nationalities
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]").click() #confirmation delete
        time.sleep(2)
        response_message = browser.find_element(By.XPATH, "//p[@data-v-89ccd62c]").text
        self.assertIn('Success', response_message)
        time.sleep(5)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
    
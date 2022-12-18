import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_1_create_MyTimesheets_positive(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)
        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)
        #open Timesheets
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[1]").click()
        time.sleep(2)
        #open My Timesheets
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']").click()
        time.sleep(2)
        #Edit data
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//div[@class='orangehrm-timesheet-footer--options']/button[1]").click()
        time.sleep(2)
       
        #Project
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("A")
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div[2]/div[1]/span").click()
        time.sleep(2)

        #Activity
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[2]/div//div[@class='oxd-select-wrapper']/div[1]//i").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div[2]/div[4]").click()
        time.sleep(2)
        
        #Comment
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[3]/div//input").send_keys("1")
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[5]/div//input").send_keys("2")
        time.sleep(2)

        #Save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//button[@type='submit']").click()
        time.sleep(3)

        #Submit
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//div[@class='orangehrm-timesheet-footer--options']/button[2]").click()
        time.sleep(2)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[1]/div[.='Submitted']").text
        self.assertEqual(response_message, 'Submitted')

    def test_2_create_MyTimesheets_negative(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)

        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)
        #open Timesheets
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[1]").click()
        time.sleep(2)
        #open My Timesheets
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']").click()
        time.sleep(2)
        #Edit data
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//div[@class='orangehrm-timesheet-footer--options']/button[1]").click()
        time.sleep(2)

        #Input data
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[3]/div//input").send_keys("1")
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[5]/div//input").send_keys("2")
        time.sleep(2)

        #Save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//button[@type='submit']").click()
        time.sleep(2)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//table/tbody/tr[1]/td[2]/div/span[.='Select an Activity']").text
        self.assertEqual(response_message, 'Select an Activity')

    def test_3_punch_in_out(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)
        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)
        #open Attendance
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(2)
        #open Punch in/out
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]/a[@role='menuitem']").click()
        time.sleep(2)
        #Punch In
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(15)
        #Punch Out
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(10)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[@class='oxd-form-actions']/p[.=' * Required']").text
        self.assertEqual(response_message, '* Required')

    def test_4_employee_records(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)
        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)
        #open Attendance
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(2)
        #open Employee records
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[3]/a[@role='menuitem']").click()
        time.sleep(2)
        #choose employee attendance records
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[4]/div[@role='row']/div[3]//button[@type='button']").click()
        time.sleep(5)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//p[.=' * Required']").text
        self.assertEqual(response_message, '* Required')   

    def test_5_configuration(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)
        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)
        #open Attendance
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(2)
        #open Configuration
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[4]/a[@role='menuitem']").click()
        time.sleep(2)
        #turn on/off configuration
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div[@class='oxd-switch-wrapper']//span").click()
        time.sleep(2) 
        #Save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(2)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//h6[.='Attendance Configuration']").text
        self.assertEqual(response_message, 'Attendance Configuration')

    def test_6_Project_Reports(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)

        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #open Reports
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(2)
        #open Project Reports
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]").click()
        time.sleep(2)
        
        # Project Name
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[1]/div/div/div//input[@placeholder='Type for hints...']").send_keys("A")
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[1]/span").click()
        time.sleep(2)

        #View
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//p[.=' * Required']").text
        self.assertEqual(response_message,'* Required')

    def test_7_Employee_Reports(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)

        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #open Reports
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(2)
        #open Employee Reports
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]").click()
        time.sleep(2)
        
        #Employee Report by employee name
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[1]/div/div/div//input[@placeholder='Type for hints...']").send_keys("A")
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[5]").click()
        time.sleep(2)

        #View
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//p[.=' * Required']").text
        self.assertEqual(response_message,'* Required')

    def test_8_Attendance_Summary(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)

        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #open Reports
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(2)
        #open Attendance Summary
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[3]").click()
        time.sleep(2)
        
        #Attendance Total Summary Report by Employee Name
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("A")
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(2)

        #View
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//h5[.='Attendance Total Summary Report']").text
        self.assertEqual(response_message,'Attendance Total Summary Report')


    def test_9_Customer_info(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)

        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)
        #open Project info
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]").click()
        time.sleep(2)
        #open Customers
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]").click()
        time.sleep(2)
        #edit data
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[4]/div/button[2]/i").click()
        time.sleep(2)

        #write description
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//textarea[@placeholder='Type description here']").send_keys("Leading Manufacturer New York")
        time.sleep(2)

        #Save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(10)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//h6[.='Customers']").text
        self.assertEqual(response_message, 'Customers')

    def test_10_Projects_info(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(3)

        #input username
        browser.find_element(By.NAME,"username").send_keys("Admin")
        #input password
        browser.find_element(By.NAME,"password").send_keys("admin123")
        #login
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        #open Time
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)
        #open Project info
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]").click()
        time.sleep(2)
        #open Projects
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]/a[@role='menuitem']").click()
        time.sleep(2)
        #edit data
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[5]/div/button[2]/i").click()
        time.sleep(2)

        #write description
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']//textarea[@placeholder='Type description here']").send_keys("First Project")
        time.sleep(2)

        #Save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(10)

        #Response message
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//h5[.='Projects']").text
        self.assertEqual(response_message, 'Projects')

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()
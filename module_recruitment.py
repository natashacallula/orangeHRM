import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestRecruitment_Candidates(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_add_candidate(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']"+
            "//div[@class='orangehrm-header-container']/button[@type='button']/i").click()
        browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Martin")
        browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Junior")
        browser.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("martinus@orange.com")
        browser.find_element(By.XPATH,"//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()

        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/form/h6').text

        self.assertIn('Application Stage', response_data)

    def test_b_delete_candidate(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']"+
            "//div[@class='orangehrm-header-container']/button[@type='button']/i").click()
        browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Martin")
        browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Junior")
        browser.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("martinus@orange.com")
        browser.find_element(By.XPATH,"//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a').click()
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]/i').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()

        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div').text

        self.assertNotIn('Martin Junior', response_data)

    def test_c_view_candidate(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']"+
            "//div[@class='orangehrm-header-container']/button[@type='button']/i").click()
        browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Martin")
        browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Junior")
        browser.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("martinus@orange.com")
        browser.find_element(By.XPATH,"//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[1]/i').click()

        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/form/h6').text

        self.assertIn('Application Stage', response_data)

    def test_d_search_candidate(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']"+
            "//div[@class='orangehrm-header-container']/button[@type='button']/i").click()
        browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Martin")
        browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Junior")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[3]').click()
        browser.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("martinus@orange.com")
        browser.find_element(By.XPATH, "//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()

        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]').text

        self.assertIn('Senior QA Lead', response_data)

    def test_e_add_vacancy(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input').send_keys("Junior Quality Assurance")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[18]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[1]/input').send_keys("Peter ")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div/span').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/button[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()

        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]').text

        self.assertIn('Junior Quality Assurance', response_data)

    def test_f_delete_vacancy(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input').send_keys("Junior Quality Assurance")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[18]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div/input').send_keys("Peter")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/button[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()

        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]').text

        self.assertNotIn('Junior Quality Assurance', response_data)

    def test_g_edit_vacancy(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input').send_keys("Junior Quality Assurance")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[18]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div/input').send_keys("Peter")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/button[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div[1]/div/div[2]/input').send_keys(Keys.CONTROL + "a",Keys.DELETE)
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div[1]/div/div[2]/input').send_keys("Payroll Administrator")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/div/div[2]/div[15]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[3]/div[1]/div/div[2]/div/div/input').send_keys(Keys.CONTROL + "a",Keys.DELETE)
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[1]/input').send_keys("Nina")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div/span').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[7]/button[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        
        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]').text

        self.assertIn('Payroll Administrator', response_data)

    def test_h_search_vacancy(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input').send_keys("Senior Quality Assurance")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[18]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div/input').send_keys("Peter")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/button[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[18]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        
        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]').text

        self.assertIn('QA Engineer', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()

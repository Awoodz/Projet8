from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from userapp.models import CustomUser


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/accounts/signup/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("testuser")
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys("testuser@mail.com")
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys("testpass1")
        password_input = self.selenium.find_element_by_name("password2")
        password_input.send_keys("testpass1")
        self.selenium.find_element_by_xpath('//button[@value="signup"]').click()
        try:
            WebDriverWait(self.selenium, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login_form"))
            )
            print("ça passe !")
            username_input = self.selenium.find_element_by_name("username")
            username_input.send_keys("testuser")
            password_input = self.selenium.find_element_by_name("password")
            password_input.send_keys("testpass1")
            self.selenium.find_element_by_xpath('//button[@value="login"]').click()
        except TimeoutError:
            print("trop tard !")

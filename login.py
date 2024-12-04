import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_login_page(self):
        """Navigates to the login page."""
        self.driver.get("https://wellfound.com/login")
        time.sleep(5)

    def fill_login_form(self, email, password):
        """Fills the login form."""
        

        password_input = self.driver.find_element(By.ID, "user_password")
        password_input.send_keys(password)

    def submit_login_form(self):
        """Submits the login form."""
        login_button = self.driver.find_element(By.NAME, "commit")
        login_button.click()
        time.sleep(5)

    def check_login_status(self):
        """Checks if login was successful by verifying the page URL."""
        if "jobs" in self.driver.current_url:
            return True
        return False

    def login(self, email, password):
        """Performs the full login process."""
        self.navigate_to_login_page()
        self.fill_login_form(email, password)
        self.submit_login_form()

        if self.check_login_status():
            print("Login successful.")
        else:
            print("Login failed.")

import os
from login import Login
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Initialize Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Login to Wellfound
login = Login(driver)
login.login(email, password)

# After login, navigate to the jobs page
driver.get("https://wellfound.com/jobs")
print("Logged in and navigated to the jobs page.")

# Close the browser
driver.quit()

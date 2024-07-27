from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
import logging

# Create a custom logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set Chrome options without headless mode
chrome_options = Options()
chrome_options.add_argument("--window-size=3697,2080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
chrome_options.add_experimental_option("useAutomationExtension", False)

# Path to the ChromeDriver executable
chrome_driver_path = "a"  # Replace with the actual path to your ChromeDriver

# Initialize the Service object
logger.debug("Initializing ChromeDriver service")
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver
logger.debug("Starting Chrome WebDriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    logger.debug("Navigating to the URL")
    driver.get("https://www.tldrthis.com/#uploadFileSection")
    logger.debug("URL loaded successfully")
    # Add your further actions here...
finally:
    logger.debug("Closing the browser")
    driver.wait()
    driver.quit()

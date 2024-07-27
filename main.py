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

import undetected_chromedriver as uc
driver = uc.Chrome(headless=True,use_subprocess=False)
driver.get('https://nowsecure.nl')

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
import linecache 
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Set the log level
logger.setLevel(logging.DEBUG)

# Create handlers for console and file outputs
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logfile.log')

# Set the log level for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(log_format)
file_handler.setFormatter(log_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Get the current date
current_date = datetime.now() + timedelta(days=7)

# Format the date as MM/DD/YYYY
formatted_date = current_date.strftime("%m/%d/%Y")

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--window-size=3697,2080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
chrome_options.add_experimental_option("useAutomationExtension", False)

# Initialize line reading counter
counter = 2


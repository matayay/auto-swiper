# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Bumble():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications":2,
            "profile.default_content_setting_values.geolocation": 1,
        })

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://bumble.com/get-started')

        time.sleep(1)

        # Switch to cookies iframe
        self.driver.switch_to.frame('sp_message_iframe_744124')
        time.sleep(1)
        # Accept cookies
        self.driver.find_element(By.XPATH, value='//*[@id="notice"]/div[2]/div[2]/div/button').click()
        time.sleep(1)
        # Switch to parent frame
        self.driver.switch_to.default_content()
        time.sleep(1)

    def login(self, user_email, user_password):
        # Login with fb.
        self.driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div').click()
        
        original_window = self.driver.current_window_handle
        
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
    
        original_window = self.driver.current_window_handle
        # Type in email
        self.driver.find_element(By.XPATH, value='//*[@id="email"]').send_keys(user_email)
        # Type in password
        self.driver.find_element(By.XPATH, value='//*[@id="pass"]').send_keys(user_password)
        # Login through fb
        self.driver.find_element(By.NAME, value='login').click()

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def likeLoop(self):
        time.sleep(8)

        while True:
            for i in range(0, 5):
                time.sleep(1)

                try:
                    # Click like button
                    self.driver.find_element(By.CLASS_NAME, value='encounters-action--like').click()

                except:
                    break

            time.sleep(2)
            try:
                # Click dislike button
                self.driver.find_element(By.CLASS_NAME, value='encounters-action--dislike').click()

            except:
                break
# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from secret import email, password

class Tinder():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications":1,
            "profile.default_content_setting_values.geolocation": 2,
        })

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://tinder.com/app/recs')

        time.sleep(1)
        # Decline cookies
        self.driver.find_element(By.XPATH, value='//*[@id="q888578821"]/div/div[2]/div/div/div[1]/div[2]/button').click()

    def login(self, user_email, user_password):
        # Login to Tinder
        self.driver.find_element(By.XPATH, value='//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
        time.sleep(2)
        #login with fb
        self.driver.find_element(By.XPATH, value='//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()

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

        time.sleep(3)
        # Location
        self.driver.find_element(By.XPATH, value='//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]').click()
        time.sleep(1)
        # Notifications
        self.driver.find_element(By.XPATH, value='//*[@id="q-839802255"]/main/div/div/div/div[3]/button[2]').click()
        time.sleep(5)
        # Lightmode
        self.driver.find_element(By.XPATH, value='//*[@id="q-839802255"]/main/div/div[2]/button').click() 

    def likeLoop(self):
        while True:
            try:
                time.sleep(2)
                # Click the like button
                self.driver.find_element(By.CSS_SELECTOR, '#q888578821 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button').click()

            except:
                time.sleep(100000)
                break

# Main Program
bot = Tinder()
bot.login(email, password)
bot.likeLoop()
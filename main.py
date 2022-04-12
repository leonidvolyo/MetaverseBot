from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
import time
import path

Path_object = path.Path()
PATH = Path_object.get_path()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# Cloudflare bypassing
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:/Users/plire/AppData/Local/Google/Chrome/User Data")
# options.add_argument('--user-data-dir=C:/Users/GOD/AppData/Local/Google/Chrome/User Data')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--no-sandbox')
options.add_argument("start-maximized")
options.add_argument('--profile-directory=Profile 3')
# options.add_argument('--headless')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(PATH), options=options)
# driver = webdriver.Chrome(options=options)
driver.get('https://www.sandbox.game/en/map/?liteMap=true&currentX=2172&currentY=3450&zoom=1')
print(driver.session_id)
time.sleep(20)
driver.refresh()
time.sleep(15)
# element = driver.find_element(By.LINK_TEXT, 'Bid')
while True:
   try:
       element = driver.find_element(By.XPATH, '//*[@id="land-details"]/div/div[3]/div/div/button')
       element.click()
       break
   except:
       print("It's okay, going forward")
#print("LAND is our!")



##########################################################################
# Attempt to get access to needed element using "MAP" element
"""time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="basic"]/div[2]/div[2]/div[1]/div[2]/div[2]/a[1]   ')
print(element)
time.sleep(5)
element.click()
time.sleep(5)"""

"""all_buttons = driver.find_elements(By.CLASS_NAME, 'navigation-button')
for i in all_buttons:
    print(i)
time.sleep(5)
for button in all_buttons:
    if button.text != "Map":
        pass
    else:
        button.click()
        time.sleep(10)"""

# WebDriverWait(driver, 20).until(presence_of_element_located(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div[1]/div[1]/div/div[3]/div/div/button'))).click()
# WebDriverWait(driver, 20).until(presence_of_element_located(driver.find_element(By.XPATH, '//button[normalize-space()="Bid"]'))).click()



##########################################################################
# Tests (Cloudflare bypassing system/finding neeeded element)
"""from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located"""
"""PATH = "C:\Program Files (x86)\chromedriver.exe
t = 2
driver = webdriver.Chrome(service=Service(PATH))
driver.get('https://www.instagram.com/')
button_prinyat = driver.find_element(By.CLASS_NAME, "aOOlW.bIiDR")
button_prinyat.click()
time.sleep(t)
button_facebook = driver.find_element(By.CLASS_NAME, "KPnG0")
button_facebook.click()
time.sleep(t)
driver.find_element(By.CLASS_NAME, "_42ft._4jy0._9xo7._4jy3._4jy1.selected._51sy").click()
driver.find_element(By.ID, "email").send_keys("leonn-07@mail.ru")
driver.find_element(By.ID, "pass").send_keys("Dinoel12345")
driver.find_element(By.NAME, "login").click()
WebDriverWait(driver, 20).until(presence_of_element_located((By.CLASS_NAME, "aOOlW.HoLwm"))).click()
"""

##########################################################################
"""driver.get('https://www.sandbox.game/')
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.TAG_NAME, "Bid")
# driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div[5]/div/div/p').click()
# driver.find_element(By.XPATH, '//button[normalize-space()="Map"]').click()
# driver.find_element(By.TAG_NAME, "p data-v-a843a35e").click()"""

##########################################################################
"""PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(service=Service(PATH))
driver.get('https://www.sandbox.game/')
driver.find_element(By.XPATH('//*[@id="sidebar"]/div/div[5]/div/div/figure')).click()
"""

##########################################################################
"""from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(PATH), options=options)
driver.get('https://www.sandbox.game')
"""

##########################################################################
"""PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=Service(PATH))
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))
driver.get('https://www.sandbox.game')
"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

# Load credentials
load_dotenv()
SPOTIFY_EMAIL = os.getenv("SPOTIFY_EMAIL")
SPOTIFY_PASSWORD = os.getenv("SPOTIFY_PASSWORD")

print("🔄 Starting browser...")
# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument("--incognito")
# Start browser with incognito mode
driver = uc.Chrome(options=options, headless=False)
driver.get("https://accounts.spotify.com/en/login")

wait = WebDriverWait(driver, 20)
print("⌛ Waiting for email input...")
email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#login-username")))
email_input.send_keys(SPOTIFY_EMAIL)
print("✅ Email entered.")

# Check if password input exists
print("🔍 Checking for password input...")

try:
    password_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#login-password"))
    )
    print("✅ Password input found.")
except:
    print("➡️ Password input not found. Clicking 'Next' button...")
    try:
        driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]').click()
        print("✅ Clicked 'Next'.")

        wait = WebDriverWait(driver, 10)
        use_password_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/form/div[2]/section/button')
        ))
        use_password_button.click()

        #driver.find_element("xpath", '/html/body/div/div/div[2]/main/div/div/div/div/form/div[2]/section/button').click()
        print("✅ Clicked 'use password button'. Waiting for password field...")
        password_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input#login-password")
        ))
        print("✅ Password field appeared.")
    except Exception as e:
        print("❌ Failed to click 'Next' or find password field:", e)
        driver.save_screenshot("next_step_error.png")
        driver.quit()
        exit()

# Enter password and click login
password_input.send_keys(SPOTIFY_PASSWORD)
print("✅ Password entered.")

print("⌛ Waiting for login button...")
try:
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div[2]/div[2]/button/span[1]').click()
    print("✅ Login button clicked.")
except Exception as e:
    print("❌ Could not click login button:", e)
    driver.save_screenshot("login_click_error.png")
    driver.quit()
    exit()


wait = WebDriverWait(driver, 10)
web_player_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div/div/div/div/button[2]')
))
web_player_button.click()

wait = WebDriverWait(driver, 10)
Like_playlist_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/nav/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]')
))
Like_playlist_button.click()
time.sleep(5)

# Scroll slowly to bottom to load all songs
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for new songs to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print("✅ Finished scrolling. Extracting song titles and artist names...")

# Get all track rows
track_rows = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tracklist-row']")

print(f"🎵 Found {len(track_rows)} songs.")

# Loop through each track row
for i, row in enumerate(track_rows, start=1):
    try:
        # Get song title
        title_elem = row.find_element(By.CSS_SELECTOR, "a[data-testid='internal-track-link'] div")
        title = title_elem.text.strip()

        # Get artist name (first artist link under row)
        artist_elem = row.find_element(By.CSS_SELECTOR, 'a[href^="/artist/"]')
        artist = artist_elem.text.strip()

        if title and artist:
            print(f"{i}. {title} — by {artist}")
    except Exception as e:
        print(f"⚠️ Skipping row {i}, error: {e}")
        
# ⏳ Wait so the browser stays open
input("🎵 Logged in or not? Check browser. Press Enter to quit...")

driver.quit()
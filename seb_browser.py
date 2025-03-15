from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import keyboard

def main():
    print("Preparing to launch browser in 1 second(s)...")
    # Add delay before opening the browser
    time.sleep(1)
    
    # First get the default user agent
    temp_options = Options()
    temp_options.add_argument("--headless=new")
    temp_driver = webdriver.Chrome(options=temp_options)
    temp_driver.get("about:blank")
    default_ua = temp_driver.execute_script("return navigator.userAgent;")
    temp_driver.quit()
    
    print(f"Default User Agent: {default_ua}")
    
    # Append SEB/1.0 to the default user agent
    modified_ua = f"{default_ua} SEB/1.0"
    print(f"Modified User Agent: {modified_ua}")
    
    print("Opening browser with modified user agent in kiosk mode...")
    # Set up Chrome with the modified user agent and kiosk mode
    chrome_options = Options()
    chrome_options.add_argument(f'--user-agent={modified_ua}')
    chrome_options.add_argument("--kiosk")  # Enable kiosk mode
    chrome_options.add_argument("--start-maximized")  # Ensure window is maximized
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Hide automation info
    chrome_options.add_experimental_option("useAutomationExtension", False)  # Disable automation extension
    
    # Initialize WebDriver with modified user agent and kiosk mode
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to the specified URL
    driver.get("https://administration.assessform.edu.au/trt/device/index?trt-return-url=")
    
    # Verify the current user agent
    current_ua = driver.execute_script("return navigator.userAgent;")
    print(f"Current User Agent: {current_ua}")
    
    # Create a flag to track if the keybind has been used
    keybind_used = False
    
    def switch_to_student_page():
        nonlocal keybind_used
        if not keybind_used:
            print("Keybind activated! Switching to student login page...")
            driver.get("https://student.assessform.edu.au/Auth/OneTimeCode?prerequisitePageViewed=true")
            keybind_used = True  # Ensure this only happens once
            print("Keybind has been used and is now disabled")
    
    # Register the hotkey (Ctrl+Shift+S)
    keyboard.add_hotkey('ctrl+shift+s', switch_to_student_page)
    
    print("Browser is open with modified user agent in kiosk mode.")
    print("Press Ctrl+Shift+S to switch to the student login page (one-time use only).")
    print("Press Ctrl+C in terminal to close the browser.")
    
    try:
        # Keep the script running
        keyboard.wait('ctrl+c')
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing browser...")
        keyboard.unhook_all()  # Remove all keyboard hooks
        driver.quit()

if __name__ == "__main__":
    main()
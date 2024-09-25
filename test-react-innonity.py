import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

@pytest.fixture
def driver_setup_teardown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def clear_input_field(element):
    element.send_keys(Keys.CONTROL + 'a')
    element.send_keys(Keys.BACKSPACE)

# Test case 1 ทดสอบการกรอกข้อมูลให้ครบถ้วน
def test_data_entry_completely(driver_setup_teardown):  
    driver = driver_setup_teardown
    driver.get('http://localhost:5173/')        # เปลี่ยนเป็น URL ของเว็บที่ต้องการทดสอบ
    
    wait = WebDriverWait(driver, 10)
    
    first_name = 'John'
    last_name = 'Doe'
    birth_date = '17-11-1998'
    email = 'JohnDoe@gmail.com'
    phone = '1234567890'
    
    input_first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[1]/div/div/input')))
    clear_input_field(input_first_name)
    input_first_name.send_keys(first_name)

    input_last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div/div/input')))
    clear_input_field(input_last_name)
    input_last_name.send_keys(last_name)

    input_birth_date = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]/div/div/input')))
    input_birth_date.send_keys(birth_date)

    input_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[5]/div/div/input')))
    clear_input_field(input_email)
    input_email.send_keys(email)

    input_phone = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[7]/div/div/input')))
    clear_input_field(input_phone)
    input_phone.send_keys(phone)
    
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div/div[6]/button')))
    submit_button.click()
    
    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        assert "บันทึกข้อมูลเรียบร้อย" in alert_text, "กรุณากรอกข้อมูลให้ครบถ้วน"
    except NoAlertPresentException:
        print("ไม่พบ Alert")
 
# Test case 2 ทดสอบการกรอกข้อมูลไม่ครบถ้วน    
def test_data_entry_incompletely(driver_setup_teardown):  
    driver = driver_setup_teardown
    driver.get('http://localhost:5173/')    # เปลี่ยนเป็น URL ของเว็บที่ต้องการทดสอบ
    
    wait = WebDriverWait(driver, 10)
    
    first_name = 'John'
    last_name = 'Doe'
    
    input_first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[1]/div/div/input')))
    clear_input_field(input_first_name)
    input_first_name.send_keys(first_name)

    input_last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div/div/input')))
    clear_input_field(input_last_name)
    input_last_name.send_keys(last_name)
    
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div/div[6]/button')))
    submit_button.click()
    
    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        assert "กรุณากรอกข้อมูลให้ครบถ้วน" in alert_text, "กรุณากรอกข้อมูลให้ครบถ้วน"
    except NoAlertPresentException:
        print("ไม่พบ Alert")
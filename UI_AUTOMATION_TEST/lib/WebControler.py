import os
from playwright.sync_api import sync_playwright
from WebElement import WebElement
from WebElementCheckboxes import WebElementCheckboxes
from WebElementDropdown import WebElementDropdown
from WebElementLogin import WebElementLogin
from WebElementUploadFile import WebElementUploadFile
import traceback
from robot.libraries.BuiltIn import BuiltIn

class WebControler:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    def __init__(self):
        self.browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=False, executable_path=self.browser_path)
            self.page = self.browser.new_page()
        except:
            raise Exception(traceback.format_exc())
        
    def open_web_page(self, url):
        self.page.goto(url)

    def login(self, username, password, is_invalid=False):
        try:
            self.page.fill(WebElementLogin.login_username(), username)
            self.page.fill(WebElementLogin.login_password(), password)
            self.page.click(WebElementLogin.login_button())
            if not is_invalid:
                self.page.wait_for_selector(WebElementLogin.login_success_message())
            else:
                self.page.wait_for_selector(WebElementLogin.login_fail_message())
        except Exception as e:
            raise Exception(traceback.format_exc())
        
    def navigate_to(self, element_locator, header_locator):
            
            element = self.page.locator(element_locator)
            element.wait_for(state="visible")

            element.click()

            self.page.locator(header_locator).wait_for(state="visible")
    
    def navigate_to_login_form(self):
        self.navigate_to(WebElement.login_form(), WebElementLogin.login_page_header())
    
    def navigate_to_check_boxes(self):
        self.navigate_to(WebElement.checkboxes(), WebElementCheckboxes.checkboxes_page_header())
    
    def navigate_to_dropdown(self):
        self.navigate_to(WebElement.dropdown(), WebElementDropdown.dropdown_page_header())
    
    def navigate_to_file_upload(self):
        self.navigate_to(WebElement.upload(), WebElementUploadFile.uploader_page_header())

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
    
    def interact_with_checkbox(self, checkbox_number, action='check'):
        checkbox = self.page.locator(WebElementCheckboxes.checkbox(checkbox_number))

        if action == 'check':
            if not checkbox.is_checked():
                checkbox.click()
        elif action == 'uncheck':
            if checkbox.is_checked():
                checkbox.click()

    def verify_checkbox_state(self, checkbox_number, expected_state='checked'):
        checkbox = self.page.locator(WebElementCheckboxes.checkbox(checkbox_number))
        if expected_state == 'checked' and checkbox.is_checked():
            print(f"{checkbox_number} is not checked.")
            return
        elif expected_state == 'unchecked' and not checkbox.is_checked():
            print(f"Check box {checkbox_number} is not unchecked.")
            return
        raise Exception(f"Check box {checkbox_number} is not {expected_state}.")
    
    def verify_dropdown_selection(self):
        try:
            dropdown_locator = self.page.locator(WebElementDropdown.dropdown_selection())
            options = dropdown_locator.locator('option').all_text_contents()

            for option_text in options:
                if option_text.strip() == 'Please select an option':
                    continue
                
                dropdown_locator.select_option(label=option_text.strip())
                
                selected_value = dropdown_locator.input_value()
                assert selected_value in option_text.strip(), f"Expected value {option_text.strip()}, but got {selected_value}"
        
        except:
            raise Exception(traceback.format_exc())

    def verify_file_upload(self, file_path=None):
        try:
            if file_path is None:
                file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)).replace("lib", "resources", 1), "some-file.txt")
            file_name = file_path.split("\\")[-1]
            print(file_name)
            self.page.locator(WebElementUploadFile.input_file_upload()).set_input_files(file_path)

            self.page.locator(WebElementUploadFile.button_submit_file_upload()).click()

            self.page.locator(WebElementUploadFile.uploaded_files(file_name)).wait_for()
        except:
            raise Exception(traceback.format_exc())
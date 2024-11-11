class WebElement:

    @staticmethod
    def login_form():
        return '//*[@id="content"]//*[text()="Form Authentication"]'
    
    @staticmethod
    def checkboxes():
        return '//*[@id="content"]//*[text()="Checkboxes"]'
    
    @staticmethod
    def dropdown():
        return '//*[@id="content"]//*[text()="Dropdown"]'
    
    @staticmethod
    def upload():
        return '//*[@id="content"]//*[text()="File Upload"]'
    

class WebElementCheckboxes:

    @staticmethod
    def checkboxes_page_header():
        return '//*[@id="content"]/div/h3[text()="Checkboxes"]'
    
    @staticmethod
    def checkbox(input_number):
        return f'//form[@id="checkboxes"]//input[@type="checkbox"][{input_number}]'
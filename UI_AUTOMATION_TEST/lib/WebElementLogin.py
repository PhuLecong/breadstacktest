class WebElementLogin:

    @staticmethod
    def login_username():
        return '//*[@id="username"]'
    
    @staticmethod
    def login_password():
        return '//*[@id="password"]'
    
    @staticmethod
    def login_button():
        return '//*[@id="login"]/button'
    
    @staticmethod
    def login_page_header():
        return '//*[@id="content"]/div/h2[text()="Login Page"]'
    
    @staticmethod
    def login_success_message():
        return '//*[@id="flash" and contains(text(),"You logged into a secure area!")]'
    
    @staticmethod
    def login_fail_message():
        return '//*[@id="flash" and (contains(text(),"Your username is invalid!") or contains(text(),"Your password is invalid!"))]'
    

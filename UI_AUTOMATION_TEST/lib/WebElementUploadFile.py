class WebElementUploadFile:

    @staticmethod
    def uploader_page_header():
        return '//*[@id="content"]/div/h3[text()="File Uploader"]'
    
    @staticmethod
    def uploaded_page_header():
        return '//*[@id="content"]/div/h3[text()="File Uploaded!"]'
    
    @staticmethod
    def input_file_upload():
        return '//*[@id="file-upload"]'

    @staticmethod
    def button_submit_file_upload():
        return '//*[@id="file-submit"]'
    
    @staticmethod
    def uploaded_files(file_name):
        return f'//*[@id="uploaded-files" and contains(text(),"{file_name}")]'
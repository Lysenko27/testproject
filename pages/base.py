

class Page(object):
    def __init__(self, driver, base_url):
      self.driver = driver
      self.driver.set_page_load_timeout(30)
      self.base_url = "https://mail.yandex.ru"


    def find_element(self, xpath):
         return self.driver.find_element_by_xpath(xpath)

    def reload_page(self):
        self.driver.execute_script("location.reload()")

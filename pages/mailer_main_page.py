from pages.base import Page

class MailerMainPage(Page):
    def __init__(self, driver):
        self.delete_xpath = "//span[@class='mail-Toolbar-Item-Text js-toolbar-item-title js-toolbar-item-title-delete']"
        self.compose_email_xpath = "//div[@class='mail-ComposeButton-Wrap']/a"
        self.message_xpath = "//div[@class='mail-MessageSnippet-Wrapper']"
        self.author_relative_path = "span.mail-MessageSnippet-FromText"
        self.subject_relative_path = "span.mail-MessageSnippet-Item_subject"
        self.mail_checkbox_relative_path = "span[class='_nb-checkbox-flag _nb-checkbox-normal-flag']"
        self.driver = driver

    def compose_email(self):
        self.driver.find_element_by_xpath(self.compose_email_xpath).click()

    def delete_selected(self):
        self.driver.find_element_by_xpath(self.delete_xpath).click()

    def go_to_folder(self, folder):
        self.driver.find_element_by_xpath(f'//a[@href="#{folder}"]').click()

    def select_email(self, number):
        self.driver.find_element_by_xpath(
          f"({self.message_xpath})[{number}]"
        ).find_element_by_css_selector(self.mail_checkbox_relative_path).click()

    def mail_on_page(self):
        return(
            list(
                map(
                    lambda e:
                        {
                            "author" : e.find_element_by_css_selector(self.author_relative_path).text,
                            "subject" : e.find_element_by_css_selector(self.subject_relative_path).text
                        },
                    list(self.driver.find_elements_by_xpath(self.message_xpath))
                    )
                )
        )

    def reload_and_fetch_mail(self):
        self.reload_page()
        return self.mail_on_page()

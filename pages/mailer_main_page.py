from helper import wait_until, mail_indexes_of
from pages.base import Page
import time
class MailerMainPage(Page):
    def __init__(self, driver):
        self.delete_xpath = "//span[@class='mail-Toolbar-Item-Text js-toolbar-item-title js-toolbar-item-title-delete']"
        self.compose_email_xpath = "//div[@class='mail-ComposeButton-Wrap']/a"
        self.message_xpath = "//div[@class='mail-MessageSnippet-Wrapper']"
        self.author_relative_path = "span.mail-MessageSnippet-FromText"
        self.subject_relative_path = "span.mail-MessageSnippet-Item_subject"
        self.mail_checkbox_relative_path = "span[class='_nb-checkbox-flag _nb-checkbox-normal-flag']"
        self.move = '//span[@class="mail-Toolbar-Item-Text js-toolbar-item-title js-toolbar-item-title-folders-actions"]'
        self.driver = driver

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

    def compose_email(self):
        self.driver.find_element_by_xpath(self.compose_email_xpath).click()

    def delete_selected(self,subject):
        self.select_email(subject)
        self.driver.find_element_by_xpath(self.delete_xpath).click()
        wait_until(lambda: len(mail_indexes_of(subject, self.reload_and_fetch_mail())), 6, 0)

    def go_to_folder(self, folder):
        self.driver.find_element_by_xpath(f'//a[@href="#{folder}"]').click()

    def select_email(self, subject):
        number= mail_indexes_of(subject, self.reload_and_fetch_mail())[0] + 1
        self.driver.find_element_by_xpath(
          f"({self.message_xpath})[{number}]").find_element_by_css_selector(self.mail_checkbox_relative_path).click()

    def move_email(self,title,subject):
        self.select_email(subject)
        self.driver.find_element_by_xpath(self.move).click()
        self.driver.find_element_by_xpath('//a[@class="b-folders__folder__link js-action" and @title="%s"]'%title).click()
        wait_until(lambda: len(mail_indexes_of(subject, self.reload_and_fetch_mail())), 6, 0)

    def go_to_folder(self,href,subject):
        self.driver.find_element_by_xpath('//a[@class="ns-view-folder ns-view-id-33 mail-NestedList-Item mail-NestedList-Item_level_1 toggles-Arrow-on-not-folded js-folders-item js-valid-drag-target fid-2" and @href="%s"]'%href).click()





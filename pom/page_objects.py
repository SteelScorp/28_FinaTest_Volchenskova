from base import seleniumbase
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class MainPageLocator:
    LOCATOR_LOGO = {'by': 'css', 'name': '#logo'}
    LOCATOR_SearchLine = {'by': 'xpath',
                          'name': '//*[@id="main_area"]/div[2]/div/div/div[3]/div/div/div/form/div/input'}
    LOCATOR_Category = {'by': 'xpath', 'name': '//*[@id="main_area"]/div[4]/div/div[4]/div/div[2]/a'}
    LOCATOR_Catalog = {'by': 'xpath', 'name': '//*[@id="main_area"]/div[2]/div/div/div[2]/a[1]/span'}
    LOCATOR_Profile = {'by': 'xpath', 'name': '//*[@id="main_area"]/div[2]/div/div/div[4]/div[1]/a/div/span'}
    LOCATOR_Bookmarks = {'by': 'xpath', 'name': '//*[@id="main_area"]/div[2]/div/div/div[4]/div[3]/a/div[1]/span'}
    LOCATOR_Basket = {'by': 'xpath', 'name': '//*[@id="main_area"]/div[2]/div/div/div[4]/div[4]/a/div[1]/span'}
    LOCATOR_Menu = {'by': 'link_text'}
    LOCATOR_SocialVK = {'by': 'xpath', 'name': '//*[@id="footer"]/div[2]/div[1]/div[2]/div[1]/a[1]'}
    LOCATOR_SocialTelegram = {'by': 'xpath', 'name': '//*[@id="footer"]/div[2]/div[1]/div[2]/div[1]/a[2]'}
    LOCATOR_SocialYoutube = {'by': 'xpath', 'name': '//*[@id="footer"]/div[2]/div[1]/div[2]/div[1]/a[3]'}
    LOCATOR_SocialOK = {'by': 'xpath', 'name': '//*[@id="footer"]/div[2]/div[1]/div[2]/div[1]/a[4]'}
    LOCATOR_ItemCode = {'by': 'xpath',
                        'name': '//*[@id="tabs_cart"]/form/table/tbody[2]/tr/td[3]/div[3]/span'}
    LOCATOR_ItemCount = {'by': 'xpath',
                         'name': '//*[@id="tabs_cart"]/form[1]/table[1]/tbody[2]/tr[1]/'
                                 'td[4]/div[1]/div[1]/span[1]/input[1]'}
    LOCATOR_ItemAmount = {'by': 'xpath', 'name': '//*[@id="tabs_cart"]/form/table/tbody[2]/tr/td[5]/div/b'}
    LOCATOR_OrderAmount = {'by': 'xpath', 'name': '//*[@id="tabs_cart"]/div[1]/div[3]/div[1]/b'}
    LOCATOR_MoreCount = {'by': 'xpath', 'name': '//*[@id="tabs_cart"]/form/table/tbody[2]/tr/td[4]/div/div/span/a[2]'}
    LOCATOR_LessCount = {'by': 'xpath', 'name': '//*[@id="tabs_cart"]/form/table/tbody[2]/tr/td[4]/div/div/span/a[1]'}
    LOCATOR_ClearBasket = {'by': 'xpath', 'name': '//*[@id="tabs_cart"]/form/div[1]/div[1]/a[2]'}
    LOCATOR_ConfirmClear = {'by': 'xpath', 'name': '//*[@id="popup_message"]/div[2]/a[1]'}
    LOCATOR_BasketCount = {'by': 'xpath', 'name': '//*[@id="main_area"]/div[2]/div/div/div[4]/div[4]/a/div[2]/span'}
    LOCATOR_CatalogItem = {'by': 'xpath',
                           'name': '//*[@id="main_area"]/div[3]/div[1]/div/div/div/div[2]/ul/li[&ListNumber]/a/span'}
    LOCATOR_SubcategoryItem = {'by': 'xpath',
                               'name': '//*[@id="main_area"]/div[4]/div/div[4]/div/div/div[&ListNumber]/a/span'}


class SearchHelper(seleniumbase.SeleniumBase):
    def __int__(self, driver):
        super().__init__(driver)

    def main_logo(self):
        return self.is_present(MainPageLocator.LOCATOR_LOGO['by'],
                               MainPageLocator.LOCATOR_LOGO['name'])

    def search_line(self):
        return self.is_present(MainPageLocator.LOCATOR_SearchLine['by'],
                               MainPageLocator.LOCATOR_SearchLine['name'])

    def catalog(self):
        return self.is_present(MainPageLocator.LOCATOR_Catalog['by'],
                               MainPageLocator.LOCATOR_Catalog['name'])

    def profile(self):
        return self.is_present(MainPageLocator.LOCATOR_Profile['by'],
                               MainPageLocator.LOCATOR_Profile['name'])

    def bookmarks(self):
        return self.is_present(MainPageLocator.LOCATOR_Bookmarks['by'],
                               MainPageLocator.LOCATOR_Bookmarks['name'])

    def basket(self):
        return self.is_present(MainPageLocator.LOCATOR_Basket['by'],
                               MainPageLocator.LOCATOR_Basket['name'])

    def menu(self, menu_name: str):
        return self.is_present(MainPageLocator.LOCATOR_Menu['by'], menu_name)

    def vk(self):
        return self.is_present(MainPageLocator.LOCATOR_SocialVK['by'],
                               MainPageLocator.LOCATOR_SocialVK['name'])

    def telegram(self):
        return self.is_present(MainPageLocator.LOCATOR_SocialTelegram['by'],
                               MainPageLocator.LOCATOR_SocialTelegram['name'])

    def youtube(self):
        return self.is_present(MainPageLocator.LOCATOR_SocialYoutube['by'],
                               MainPageLocator.LOCATOR_SocialYoutube['name'])

    def ok(self):
        return self.is_present(MainPageLocator.LOCATOR_SocialOK['by'],
                               MainPageLocator.LOCATOR_SocialOK['name'])

    def enter_word(self, word: str) -> WebElement:
        search_field = self.is_present(MainPageLocator.LOCATOR_SearchLine['by'],
                                       MainPageLocator.LOCATOR_SearchLine['name'])
        search_field.send_keys(word)
        search_field.send_keys(Keys.ENTER)
        return self.is_present(MainPageLocator.LOCATOR_Category['by'],
                               MainPageLocator.LOCATOR_Category['name'])

    def add_to_basket(self):
        self.is_present(MainPageLocator.LOCATOR_Menu['by'], 'Купить').click()
        # чтобы перейти в корзину минуя модальное окно, нужно 2 клика
        self.is_present(MainPageLocator.LOCATOR_Basket['by'], MainPageLocator.LOCATOR_Basket['name']).click()
        self.is_present(MainPageLocator.LOCATOR_Basket['by'], MainPageLocator.LOCATOR_Basket['name']).click()
        return

    def item_code(self):
        return self.is_present(MainPageLocator.LOCATOR_ItemCode['by'],
                               MainPageLocator.LOCATOR_ItemCode['name'])

    def item_count(self):
        return self.is_present(MainPageLocator.LOCATOR_ItemCount['by'],
                               MainPageLocator.LOCATOR_ItemCount['name'])

    def item_amount(self):
        return self.is_present(MainPageLocator.LOCATOR_ItemAmount['by'],
                               MainPageLocator.LOCATOR_ItemAmount['name'])

    def order_amount(self):
        return self.is_present(MainPageLocator.LOCATOR_OrderAmount['by'],
                               MainPageLocator.LOCATOR_OrderAmount['name'])

    def more_count(self):
        return self.is_present(MainPageLocator.LOCATOR_MoreCount['by'],
                               MainPageLocator.LOCATOR_MoreCount['name'])

    def less_count(self):
        return self.is_present(MainPageLocator.LOCATOR_LessCount['by'],
                               MainPageLocator.LOCATOR_LessCount['name'])

    def clear_basket(self):
        self.is_present(MainPageLocator.LOCATOR_ClearBasket['by'],
                        MainPageLocator.LOCATOR_ClearBasket['name']).click()
        self.is_present(MainPageLocator.LOCATOR_ConfirmClear['by'],
                        MainPageLocator.LOCATOR_ConfirmClear['name']).click()
        return

    def basket_count(self):
        return self.is_present(MainPageLocator.LOCATOR_BasketCount['by'],
                               MainPageLocator.LOCATOR_BasketCount['name'])

    def catalog_item(self, item_num: str):
        return self.is_present(MainPageLocator.LOCATOR_CatalogItem['by'],
                               MainPageLocator.LOCATOR_CatalogItem['name'].replace('&ListNumber', item_num))

    def subcategory_item(self, item_num: str):
        return self.is_present(MainPageLocator.LOCATOR_SubcategoryItem['by'],
                               MainPageLocator.LOCATOR_SubcategoryItem['name'].replace('&ListNumber', item_num))

import pytest
from pom import page_objects


@pytest.mark.usefixtures('setup')
class TestHomepage:

    # тест1: Присутствует элемент главной страницы - Логотип
    def test_main_page_open(self):
        page_objects.SearchHelper(self.driver).main_logo()

    # тест2: Присутствует элемент главной страницы - Строка поиска
    def test_search_line(self):
        page_objects.SearchHelper(self.driver).search_line()

    # тест3: Присутствует элемент главной страницы - Каталог
    def test_catalog(self):
        page_objects.SearchHelper(self.driver).catalog()

    # тест4: Присутствует элемент главной страницы - Вход/Регистрация
    def test_profile(self):
        page_objects.SearchHelper(self.driver).profile()

    # тест5: Присутствует элемент главной страницы - Закладки
    def test_bookmarks(self):
        page_objects.SearchHelper(self.driver).bookmarks()

    # тест6: Присутствует элемент главной страницы - Корзина
    def test_basket(self):
        page_objects.SearchHelper(self.driver).basket()

    # тест7: Присутствует пункт меню подвала - О компании
    def test_company_menu(self):
        page_objects.SearchHelper(self.driver).menu('О компании')

    # тест8: Присутствует пункт меню подвала - Вакансии
    def test_hr_menu(self):
        page_objects.SearchHelper(self.driver).menu('Вакансии')

    # тест9: Присутствует пункт меню подвала - Дилерам
    def test_dealer_menu(self):
        page_objects.SearchHelper(self.driver).menu('Дилерам')

    # тест10: Присутствует пункт меню подвала - Для прессы
    def test_press_menu(self):
        page_objects.SearchHelper(self.driver).menu('Для прессы')

    # тест11: Присутствует пункт меню подвала - О компании
    def test_news_menu(self):
        page_objects.SearchHelper(self.driver).menu('Новости')

    # тест12: Присутствует пункт меню подвала - Помощь и поддержка
    def test_help_menu(self):
        page_objects.SearchHelper(self.driver).menu('Помощь и поддержка')

    # тест13: Присутствует пункт меню подвала - Политика конфиденциальности
    def test_privacy_menu(self):
        page_objects.SearchHelper(self.driver).menu('Политика конфиденциальности')

    # тест14: Присутствует пункт меню подвала - Доставка
    def test_delivery_menu(self):
        page_objects.SearchHelper(self.driver).menu('Доставка')

    # тест15: Проверка присутствия пунктов верхнего меню
    def test_upper_menu(self):
        menu_items = ["Как купить", "Клуб ON-бонус", "Помощь", "Гарантия", "Пункты выдачи", "Для бизнеса"]
        for item in menu_items:
            page_objects.SearchHelper(self.driver).menu(item)

    # тест16: пункт меню подвала "Закладки" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_bookmarks_click(self):
        page_objects.SearchHelper(self.driver).bookmarks().click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест17: пункт меню подвала "Корзина" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_basket_click(self):
        page_objects.SearchHelper(self.driver).basket().click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест18: пункт меню подвала "О компании" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_company_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('О компании').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест19: пункт меню подвала "Вакансии" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_hr_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('Вакансии').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест20: пункт меню подвала "Дилерам" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_dealer_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('Дилерам').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест21: пункт меню подвала "Для прессы" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_press_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('Для прессы').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест22: пункт меню подвала "Новости" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_news_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('Новости').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест23: пункт меню подвала "Помощь и поддержка" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_help_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('Помощь и поддержка').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест24: пункт меню подвала "Политика конфиденциальности" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_privacy_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('Политика конфиденциальности').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест25: пункт меню подвала "Доставка" кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_delivery_menu_click(self):
        page_objects.SearchHelper(self.driver).menu('Доставка').click()
        assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест26: каждый пункт верхнего меню кликабелен и осуществляется переход
    # на другую страницу (ссылка отличается от главной)
    def test_upper_menu_click(self):
        menu_items = ["Как купить", "Клуб ON-бонус", "Помощь", "Гарантия", "Пункты выдачи", "Для бизнеса"]
        for item in menu_items:
            page_objects.SearchHelper(self.driver).menu(item).click()
            assert self.driver.current_url != 'https://www.onlinetrade.ru/'

    # тест27: Проверка наличия ссылки на ВКонтакте и ее корректности
    def test_vk(self):
        assert page_objects.SearchHelper(self.driver).vk().get_attribute('href') == \
               'https://www.vk.com/onlinetrade'

    # тест28: Проверка наличия ссылки на Telegram и ее корректности
    def test_telegram(self):
        assert page_objects.SearchHelper(self.driver).telegram().get_attribute('href') == \
               'https://t.me/onlinetradeshopru'

    # тест29: Проверка наличия ссылки на YouTube и ее корректности
    def test_youtube(self):
        assert page_objects.SearchHelper(self.driver).youtube().get_attribute('href') == \
               'https://www.youtube.com/c/onlinetraderu'

    # тест30: Проверка наличия ссылки на Одноклассники и ее корректности
    def test_ok(self):
        assert page_objects.SearchHelper(self.driver).ok().get_attribute('href') == \
               'https://ok.ru/group/68866316828710'

    # тест31: Работоспособность поиска -
    # Найти строку поиска -> написать запрос "word" -> нажать "Enter" ->
    # Убедиться в переходе на страницу с категориями и наличием кнопки "Искать среди товаров"
    def test_search_word(self):
        page_objects.SearchHelper(self.driver).enter_word('чайник')

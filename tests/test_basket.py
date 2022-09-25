import pytest
from pom import page_objects


@pytest.mark.usefixtures('setup')
class TestBasket:

    # тест1: Проверка изменения счетчика товаров в корзине -
    # при добавлении одного товара счетчик меняется
    def test_basket_count_change(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        basket_count = page_objects.SearchHelper(self.driver).basket_count().text
        assert int(basket_count) > 0

    # тест2: Проверка счетчика товаров в корзине -
    # при добавлении трех товаров в корзину счетчик равен 3
    def test_basket_count_change2(self):
        item_add_count = 0
        for i in range(3):
            page_objects.SearchHelper(self.driver).menu('Купить').click()
            item_add_count += 1
            page_objects.SearchHelper(self.driver).main_logo().click()
            page_objects.SearchHelper(self.driver).main_logo().click()
        basket_count = page_objects.SearchHelper(self.driver).basket_count().text
        assert item_add_count == int(basket_count)

    # тест3: Добавление товара в корзину -
    # Найти первый товар -> нажать "Купить" -> перейти в "Корзину" ->
    # Убедиться что есть товар, получив его атрибут "Код товара: ХХХХХ"
    def test_add_to_basket(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        assert 'Код товара:' in page_objects.SearchHelper(self.driver).item_code().text

    # тест4: У добавленного товара в корзину проверить, что сумма = сумме заказа ИТОГО
    def test_order_amount(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        item_amount = page_objects.SearchHelper(self.driver).item_amount()
        order_amount = page_objects.SearchHelper(self.driver).order_amount()
        assert item_amount.text == order_amount.text

    # тест5: Увеличение количества товара в корзине -
    # Найти первый товар -> нажать "Купить" -> перейти в "Корзину" -> Нажать "+"
    # Убедиться кол-во товара увеличилось
    def test_more_count(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        item_count = page_objects.SearchHelper(self.driver).item_count().get_attribute('value')
        page_objects.SearchHelper(self.driver).more_count().click()
        item_count_more = page_objects.SearchHelper(self.driver).item_count().get_attribute('value')
        assert item_count_more > item_count

    # тест6: Уменьшение количества товара в корзине -
    # Найти первый товар -> нажать "Купить" -> перейти в "Корзину" -> Нажать "+" -> Нажать "-"
    # Убедиться кол-во товара уменьшилось
    def test_less_count(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        page_objects.SearchHelper(self.driver).more_count().click()
        item_count_more = page_objects.SearchHelper(self.driver).item_count().get_attribute('value')
        page_objects.SearchHelper(self.driver).less_count().click()
        item_count_less = page_objects.SearchHelper(self.driver).item_count().get_attribute('value')
        assert item_count_less < item_count_more

    # тест7: Уменьшение количества товара в корзине менее 1 -
    # Найти первый товар -> нажать "Купить" -> перейти в "Корзину" -> Нажать "-"
    # Убедиться, что кол-во товара нельзя уменьшить менее 1
    def test_negative_less_count(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        item_count = page_objects.SearchHelper(self.driver).item_count().get_attribute('value')
        page_objects.SearchHelper(self.driver).less_count().click()
        item_count_less = page_objects.SearchHelper(self.driver).item_count().get_attribute('value')
        assert item_count_less == item_count

    # тест8: У добавленного товара в корзину проверить, что меняется сумма при увеличении кол-ва
    def test_item_amount_change_more(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        item_amount = page_objects.SearchHelper(self.driver).item_amount().text
        page_objects.SearchHelper(self.driver).more_count().click()
        item_amount_more = page_objects.SearchHelper(self.driver).item_amount().text
        assert item_amount != item_amount_more

    # тест9: У добавленного товара в корзину проверить, что меняется сумма при уменьшении кол-ва
    def test_item_amount_change_less(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        page_objects.SearchHelper(self.driver).more_count().click()
        item_amount = page_objects.SearchHelper(self.driver).item_amount().text
        page_objects.SearchHelper(self.driver).less_count().click()
        item_amount_less = page_objects.SearchHelper(self.driver).item_amount().text
        assert item_amount != item_amount_less

    # тест10: У добавленного товара в корзину проверить, что меняется сумма заказа ИТОГО при увеличении кол-ва
    def test_order_amount_change_more(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        order_amount = page_objects.SearchHelper(self.driver).order_amount().text
        page_objects.SearchHelper(self.driver).more_count().click()
        order_amount_more = page_objects.SearchHelper(self.driver).order_amount().text
        assert order_amount != order_amount_more

    # тест11: У добавленного товара в корзину проверить, что меняется сумма заказа ИТОГО при уменьшении кол-ва
    def test_order_amount_change_less(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        page_objects.SearchHelper(self.driver).more_count().click()
        order_amount = page_objects.SearchHelper(self.driver).order_amount().text
        page_objects.SearchHelper(self.driver).less_count().click()
        order_amount_less = page_objects.SearchHelper(self.driver).order_amount().text
        assert order_amount != order_amount_less

    # тест12: Проверка очистки корзины:
    # Найти первый товар -> нажать "Купить" -> перейти в "Корзину" -> Нажать "Очистить корзину" ->
    # Нажать "подтвердить очистку" - Убедиться, что кол-во товара в корзине = 0
    def test_clear_basket(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        page_objects.SearchHelper(self.driver).clear_basket()
        basket_count = page_objects.SearchHelper(self.driver).basket_count().text
        assert int(basket_count) == 0

    # тест13: У добавленного товара в корзину проверить, что при изменении кол-ва
    # сумма меняется кратно
    def test_item_count_amount_change(self):
        page_objects.SearchHelper(self.driver).add_to_basket()
        item_amount = int(page_objects.SearchHelper(self.driver).item_amount().text
                          .replace(' ₽', '').replace(' ', ''))
        page_objects.SearchHelper(self.driver).more_count().click()
        item_amount_x2 = int(page_objects.SearchHelper(self.driver).item_amount().text
                             .replace(' ₽', '').replace(' ', ''))
        assert item_amount_x2 / 2 == item_amount

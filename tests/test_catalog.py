import pytest
from pom import page_objects


@pytest.mark.usefixtures('setup')
class TestCatalog:

    # тест1: Открывается каталог и присутствует хотя бы 1 категория
    def test_catalog_1st_category(self):
        page_objects.SearchHelper(self.driver).catalog().click()
        page_objects.SearchHelper(self.driver).catalog_item(str(1))

    # тест2: Открывается каталог и присутствуют все 19 категорий
    def test_catalog_all_categories(self):
        page_objects.SearchHelper(self.driver).catalog().click()
        for category_num in range(1, 20):
            page_objects.SearchHelper(self.driver).catalog_item(str(category_num))

    # тест3: Имена всех категорий соответствуют заданным
    def test_catalog_all_categories_names(self):
        category_names = ["Электроника",
                          "Компьютеры и периферия",
                          "Бытовая техника",
                          "Строительство и ремонт",
                          "Товары для дома",
                          "Дача, сад и огород",
                          "Мебель и свет",
                          "Офисная техника",
                          "Автотовары",
                          "Спорт, отдых, туризм",
                          "Красота и здоровье",
                          "Детские товары",
                          "Зоотовары",
                          "Продукты питания",
                          "Одежда, обувь и аксессуары",
                          "Хобби, творчество, книги",
                          "Часы, сувениры, подарки",
                          "Аптека",
                          "Уценка"]
        page_objects.SearchHelper(self.driver).catalog().click()
        for category_num in range(1, 20):
            assert page_objects.SearchHelper(self.driver).catalog_item(str(category_num)).text in category_names

    # тест4: По всем 19ти категориям осуществляется переход на соответствующие страницы
    def test_catalog_all_categories_link(self):
        for category_num in range(1, 20):
            page_objects.SearchHelper(self.driver).catalog().click()
            page_objects.SearchHelper(self.driver).catalog_item(str(category_num)).click()
            assert self.driver.current_url != 'https://www.onlinetrade.ru/'
            page_objects.SearchHelper(self.driver).main_logo().click()

    # тест5: У каждой из 18 (кроме "Уценка") основных категорий каталога присутствует
    # хотя бы 1 подкатегория
    def test_subcategory_all_categories(self):
        for category_num in range(1, 19):
            page_objects.SearchHelper(self.driver).catalog().click()
            page_objects.SearchHelper(self.driver).catalog_item(str(category_num)).click()
            page_objects.SearchHelper(self.driver).subcategory_item(str(int(1)))
            page_objects.SearchHelper(self.driver).main_logo().click()

    # тест6: Количество подкатегорий у каждой из 18 (кроме "Уценка") основных категорий каталога
    # соответствует заданному
    def test_subcategory_count(self):
        subcategories_count_list = {"Электроника": 9,
                                    "Компьютеры и периферия": 12,
                                    "Бытовая техника": 9,
                                    "Строительство и ремонт": 15,
                                    "Товары для дома": 17,
                                    "Дача, сад и огород": 19,
                                    "Мебель и свет": 9,
                                    "Офисная техника": 11,
                                    "Автотовары": 15,
                                    "Спорт, отдых, туризм": 17,
                                    "Красота и здоровье": 14,
                                    "Детские товары": 13,
                                    "Зоотовары": 9,
                                    "Продукты питания": 10,
                                    "Одежда, обувь и аксессуары": 6,
                                    "Хобби, творчество, книги": 16,
                                    "Часы, сувениры, подарки": 3,
                                    "Аптека": 14}
        for category_num in range(1, 19):
            page_objects.SearchHelper(self.driver).catalog().click()
            category = page_objects.SearchHelper(self.driver).catalog_item(str(category_num))
            subcategory_key = category.text
            category.click()
            for subcategory_num in range(1, subcategories_count_list.get(subcategory_key) + 1):
                page_objects.SearchHelper(self.driver).subcategory_item(str(subcategory_num))
            page_objects.SearchHelper(self.driver).main_logo().click()

    # тест7: Проверка перехода в каждую подкатегорию (2-й уровень дерева каталогов)
    # каждой из 18 (кроме "Уценка") основных категорий каталога
    # !!! Длительность теста 5 минут
    def test_subcategory_link(self):
        subcategories_count_list = {"Электроника": 9,
                                    "Компьютеры и периферия": 12,
                                    "Бытовая техника": 9,
                                    "Строительство и ремонт": 15,
                                    "Товары для дома": 17,
                                    "Дача, сад и огород": 19,
                                    "Мебель и свет": 9,
                                    "Офисная техника": 11,
                                    "Автотовары": 15,
                                    "Спорт, отдых, туризм": 17,
                                    "Красота и здоровье": 14,
                                    "Детские товары": 13,
                                    "Зоотовары": 9,
                                    "Продукты питания": 10,
                                    "Одежда, обувь и аксессуары": 6,
                                    "Хобби, творчество, книги": 16,
                                    "Часы, сувениры, подарки": 3,
                                    "Аптека": 14}
        for category_num in range(1, 19):
            page_objects.SearchHelper(self.driver).catalog().click()
            category = page_objects.SearchHelper(self.driver).catalog_item(str(category_num))
            subcategory_key = category.text
            category.click()
            category_link = self.driver.current_url
            for subcategory_num in range(1, subcategories_count_list.get(subcategory_key) + 1):
                page_objects.SearchHelper(self.driver).subcategory_item(str(subcategory_num)).click()
                subcategory_link = self.driver.current_url
                assert subcategory_link != category_link
                self.driver.back()
            page_objects.SearchHelper(self.driver).main_logo().click()

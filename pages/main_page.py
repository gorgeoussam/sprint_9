import time
from allure import step

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.MAIN_URL)
        self.wait_for_clickable_element(MainPageLocators.ROOT_FIELD)

    @step("Ввод адреса 'Откуда'")
    def enter_address_from(self, address):
        self.input_to_element(MainPageLocators.INPUT_FROM, address)

    @step("Ввод адреса 'Куда'")
    def enter_address_to(self, address):
        self.input_to_element(MainPageLocators.INPUT_TO, address)

    @step("Получение точек")
    def check_points_visibility(self):
        self.wait_for_clickable_element(MainPageLocators.POINTS)
        points = self.find_element(MainPageLocators.POINTS)
        if len(points) == 2:
            return True
        return False

    @step("Загрузка блока с маршрутами")
    def is_route_visible(self):
        self.wait_for_load_element(MainPageLocators.ROUTES_OPTIONS)
        return True

    @step("Ожидание загрузки блока с маршрутами под адресами")
    def is_route_picker_visible(self):
        self.wait_for_clickable_element(MainPageLocators.CHOOSE_ROUTES_BLOCK)
        return True

    @step("Получение цены поездки")
    def get_price(self):
        self.wait_for_load_element(MainPageLocators.PRICE_TEXT)
        return self.find_element(MainPageLocators.PRICE_TEXT)

    @step("получение длительности поездки")
    def get_duration(self):
        self.wait_for_load_element(MainPageLocators.DURATION_TEXT)
        return self.find_element(MainPageLocators.DURATION_TEXT)

    def get_optimal_route(self):
        self.wait_for_load_element(MainPageLocators.OPTIMAL_BLOCK)
        return self.find_element(MainPageLocators.OPTIMAL_BLOCK)

    def get_fast_route(self):
        self.wait_for_load_element(MainPageLocators.FAST_BLOCK)
        return self.find_element(MainPageLocators.FAST_BLOCK)

    def get_self_route(self):
        self.wait_for_load_element(MainPageLocators.SELF_BLOCK)
        return self.find_element(MainPageLocators.SELF_BLOCK)

    @step("Выбрать оптимальный режим")
    def click_optimal_route(self):
        self.get_optimal_route().click()

    @step("Выбрать быстрый режим")
    def click_fast_route(self):
        self.get_fast_route().click()

    @step("Выбрать свой режим")
    def click_self_route(self):
        self.get_self_route().click()

    def get_vehicle_types(self):
        self.wait_for_load_element(MainPageLocators.VEHICLE_TYPES)
        return self.find_elements(MainPageLocators.VEHICLE_TYPES)

    def is_call_taxi_button_clickable(self):
        self.wait_for_clickable_element(MainPageLocators.CALL_TAXI_BTN)
        return True

    def is_book_drive_btn_clickable(self):
        self.wait_for_clickable_element(MainPageLocators.BOOK_DRIVE_BTN)
        return True

    @step("Выбрать тип транспортного средства Драйв")
    def choose_drive_vehicle_types(self):
        self.wait_for_load_element(MainPageLocators.VEHICLE_TYPES)
        self.wait_for_clickable_element(MainPageLocators.VEHICLE_TYPES_DRIVE)
        self.click_element(MainPageLocators.VEHICLE_TYPES_DRIVE)

    @step("Нажать кнопку 'Вызвать такси' в режиме Быстрый")
    def click_call_taxi_btn(self):
        self.wait_for_clickable_element(MainPageLocators.CALL_TAXI_BTN)
        self.click_element(MainPageLocators.CALL_TAXI_BTN)

    def get_tariff_types(self):
        self.wait_for_load_element(MainPageLocators.TARIFF_TYPES)
        return self.find_elements(MainPageLocators.TARIFF_TYPES)

    def is_tariff_picker_loaded(self):
        self.wait_for_load_element(MainPageLocators.TARIFF_PICKER)
        return True

    def get_tariff_title(self, tariff):
        return tariff.find_element(*MainPageLocators.TARIFF_TYPE_TITLE).text

    def get_tariff_description(self, tariff):
        tariff.click()
        self.wait_for_clickable_element(tariff.find_element(*MainPageLocators.TARIFF_TYPE_INFO))

        info_btn = tariff.find_element(*MainPageLocators.TARIFF_TYPE_INFO)
        self.move_mouse_to_element(info_btn)
        self.wait_for_load_element(MainPageLocators.TARIFF_TYPE_DESCRIPTION_SHOW)
        return self.find_element(MainPageLocators.TARIFF_TYPE_DESCRIPTION).text

    def is_phone_loaded(self):
        self.wait_for_load_element(MainPageLocators.PHONE)
        return True

    def is_payment_method_loaded(self):
        self.wait_for_load_element(MainPageLocators.PAYMENT_METHOD)
        return True

    def is_comment_loaded(self):
        self.wait_for_load_element(MainPageLocators.COMMENT)
        return True

    def is_requirements_loaded(self):
        self.wait_for_load_element(MainPageLocators.ORDER_REQUIREMENT)
        return True

    def get_tariff_price(self, tariff):
        return tariff.find_element(*MainPageLocators.TARIFF_TYPE_PRICE).text

    @step("Раскрыть форму 'Требования к заказу'")
    def open_requirements(self):
        self.wait_for_clickable_element(MainPageLocators.ORDER_REQUIREMENT)
        self.click_element(MainPageLocators.ORDER_REQUIREMENT)

    @step("Включить чек-бокс 'Столик для ноутбука'")
    def choose_laptop_table(self):
        self.scroll_to_element(MainPageLocators.CHOOSE_LAPTOP)
        self.wait_for_clickable_element(MainPageLocators.CHOOSE_LAPTOP)
        self.click_element(MainPageLocators.CHOOSE_LAPTOP)

    @step("Кликнуть по кнопке 'Ввести номер и заказать'")
    def click_order_btn(self):
        self.wait_for_clickable_element(MainPageLocators.TAXI_ORDER_BTN)
        self.click_element(MainPageLocators.TAXI_ORDER_BTN)

    def wait_for_order_to_be_ready(self):
        self.wait_for_load_element(MainPageLocators.ORDER_NUMBER, timeout=40)

    @step("Открыть детали маршрута")
    def open_trip_details(self):
        self.wait_for_clickable_element(MainPageLocators.TRIP_DETAIL_BTN)
        self.click_element(MainPageLocators.TRIP_DETAIL_BTN)

    def get_price_from_trip_details(self):
        self.wait_for_load_element(MainPageLocators.FINAl_PRICE)
        price = self.find_element(MainPageLocators.FINAl_PRICE).text
        prefix = "Стоимость - "
        return price[len(prefix):]

    @step("Кликнуть по кнопке 'Отменить'")
    def cancel_trip(self):
        self.wait_for_clickable_element(MainPageLocators.CANCEL_TRIP_BTN)
        self.click_element(MainPageLocators.CANCEL_TRIP_BTN)

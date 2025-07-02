from allure import title
from data import test_data
from pages.main_page import MainPage

class TestMainFunctionality:
    @title("Проверка отображения двух точек маршрута")
    def check_points_visibility(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        assert page.check_points_visibility()

    @title("Проверка отображения блока маршрута")
    def test_routes_visible(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        assert page.is_route_visible()

    @title("Проверка отображения блока маршрута под адресами")
    def test_routes_picker_visible(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        assert page.is_route_picker_visible()

    @title("Проверка отображения цены и длительности при одинаковых адресах")
    def test_price_and_duration(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.FIRST_ADDRESS)

        price = page.get_price()
        duration = page.get_duration()

        assert price.text == "Авто Бесплатно"
        assert duration.text == "В пути 0 мин."

    @title("Проверка изменения стоимости при переключении маршрутов")
    def test_updating_price_and_duration(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)

        price_fast = page.get_price().text
        duration_fast = page.get_duration().text
        print(price_fast, duration_fast)

        page.click_optimal_route()
        optimal_btn = page.get_optimal_route()

        assert "active" in optimal_btn.get_attribute("class")

        price_optimal = page.get_price().text
        duration_optimal = page.get_duration().text
        print(price_optimal, duration_optimal)
        assert price_fast != price_optimal, "Стоимость не пересчитывется"
        assert duration_fast != duration_optimal, "Продолжительность не пересчитывается или не изменилась"

    @title("Проверка активности типов траспорта в режиме Свой")
    def test_active_vehicle_types(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)

        page.click_self_route()
        assert "active" in page.get_self_route().get_attribute("class")

        for vt in page.get_vehicle_types():
            assert "disabled" not in vt.get_attribute("class")

    @title("Проверка активности кнопки вызова такси в режиме Быстрый")
    def test_call_taxi_btn_active(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)

        assert page.is_call_taxi_button_clickable()


    @title("Проверка активности кнопки Забронировать в режиме Свой-Драйв")
    def test_book_drive_btn_active(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        page.click_self_route()
        page.choose_drive_vehicle_types()

        assert page.is_book_drive_btn_clickable()

    @title("Проверка отображения тарифов такси")
    def test_taxi_tariff_active(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        page.click_call_taxi_btn()

        assert page.is_tariff_picker_loaded()

        tariff_types = page.get_tariff_types()
        assert len(tariff_types) == 6

        has_active = False
        for tt in tariff_types:
            has_active = "active" in tt.get_attribute("class")
            if has_active:
                break
        assert has_active

    def test_taxi_tariff_active(self, driver):
        page = MainPage(driver)
        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        page.click_call_taxi_btn()

        assert page.is_tariff_picker_loaded()

        tariff_types = page.get_tariff_types()
        assert len(tariff_types) == 6

        has_active = any("active" in tt.get_attribute("class") for tt in tariff_types)
        assert has_active

    @title("Проверка названия тарифов такси по ТЗ")
    def test_taxi_tariff_title(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        page.click_call_taxi_btn()

        for tariff in page.get_tariff_types():
            assert page.get_tariff_title(tariff) in test_data.TARIFF_DESCRIPTION

    @title("Проверка всплывающего окна с описанием тарифа по ТЗ")
    def test_taxi_tariff_description_show(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        page.click_call_taxi_btn()

        for tariff in page.get_tariff_types():
            title = page.get_tariff_title(tariff)
            description = page.get_tariff_description(tariff)
            assert test_data.TARIFF_DESCRIPTION[title] == description

    @title("Проверка загрузки формы заказа такси по ТЗ")
    def test_taxi_order_form_loaded(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        page.click_call_taxi_btn()

        assert page.is_phone_loaded()
        assert page.is_payment_method_loaded()
        assert page.is_comment_loaded()
        assert page.is_requirements_loaded()

    @title("Проверка заказа такси")
    def test_taxi_order(self, driver):
        page = MainPage(driver)

        page.enter_address_from(test_data.FIRST_ADDRESS)
        page.enter_address_to(test_data.SECOND_ADDRESS)
        page.click_call_taxi_btn()

        tariff = page.get_tariff_types()[0]
        price = page.get_tariff_price(tariff).replace(" ", "")

        page.open_requirements()
        page.choose_laptop_table()
        page.click_order_btn()
        page.wait_for_order_to_be_ready()
        page.open_trip_details()

        new_price = page.get_price_from_trip_details()
        assert price == new_price

        page.cancel_trip()
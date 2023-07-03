import pytest
from selenium.webdriver.common.by import By

CREATED_PETS_COUNT = 3

def test_show_my_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('bobo@mail.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('sirius')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, ".card-deck .card-text")
    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_all_pets_present_on_my_page(my_pets_profile_page, wait_profile_cards, wait_table_cards):
    profile_cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    table_cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    profile_numbers = int(profile_cards[0].text.split('\n')[1].split()[1])
    assert profile_numbers == len(table_cards)


def test_half_of_cards_with_photo(my_pets_profile_page, wait_profile_cards):
    profile_cards = pytest.driver.find_elements(
        By.CSS_SELECTOR,
        '.\\.col-sm-4.left'
    )
    images = pytest.driver.find_elements(
        By.CSS_SELECTOR,
        '.table.table-hover img'
    )
    profile_numbers = profile_cards[0].text.split('\n')
    profile_numbers = int(profile_numbers[1].split()[1])
    cards_with_photo = 0
    for index, image in enumerate(images):
        if image.get_attribute('src') != '':
            cards_with_photo += 1
    assert cards_with_photo >= profile_numbers // 2


def test_pets_have_image_name_descriptions(my_pets_profile_page, wait_table_cards):
    table_cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    for i, n in enumerate(table_cards):
        cards_content = n.text.replace('\n', '').replace('×', '').split()
        assert len(cards_content) == CREATED_PETS_COUNT


def test_pets_card_have_unique_names(my_pets_profile_page, wait_table_cards):
    table_cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    names = [n.text.replace('\n', '').replace('×', '').split()[0] for i, n in enumerate(table_cards)]
    count = 0
    for i, n in enumerate(names):
        if names.count(n) > 1:
            count += 1
    assert count == 0


def test_no_duplicate_on_my_pets_cards(my_pets_profile_page, wait_table_cards):
    table_cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    cards_content = [d.text.replace('\n', '').replace('×', '').split() for i, d in enumerate(table_cards)]
    line = ''
    for i in cards_content:
        line += ''.join(i) + ' '
    full_numbers = len(line.split())
    unique_numbers = len(set(line.split()))
    assert (full_numbers - unique_numbers) == 0

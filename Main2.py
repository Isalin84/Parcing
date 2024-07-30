from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_user_input(prompt):
    return input(prompt).strip()

def print_paragraphs(browser):
    paragraphs = browser.find_elements(By.CSS_SELECTOR, "p")
    for i, p in enumerate(paragraphs, start=1):
        print(f"{i}. {p.text}")
        if i % 5 == 0:
            cont = get_user_input("Нажмите Enter для продолжения или 'q' для выхода: ")
            if cont.lower() == 'q':
                break

def list_internal_links(browser):
    links = browser.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    for i, link in enumerate(links, start=1):
        print(f"{i}. {link.text} ({link.get_attribute('href')})")
    return links

def navigate_to_link(browser, links):
    try:
        choice = int(get_user_input("Введите номер ссылки, чтобы перейти на страницу: "))
        if 1 <= choice <= len(links):
            link = links[choice - 1]
            browser.get("https://ru.wikipedia.org" + link.get_attribute('href'))
            time.sleep(2)  # Ожидание загрузки страницы
        else:
            print("Неверный выбор. Попробуйте снова.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите номер.")

def main():
    browser = webdriver.Chrome()

    try:
        query = get_user_input("Введите ваш запрос: ")
        search_url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
        browser.get(search_url)
        time.sleep(2)  # Ожидание загрузки страницы

        while True:
            action = get_user_input("Выберите действие:\n1. Листать параграфы текущей статьи\n2. Перейти на одну из связанных страниц\n3. Выйти из программы\nВведите номер действия: ")

            if action == '1':
                print_paragraphs(browser)
            elif action == '2':
                links = list_internal_links(browser)
                if links:
                    navigate_to_link(browser, links)
            elif action == '3':
                print("Спасибо за использование программы!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
    finally:
        browser.quit()

if __name__ == "__main__":
    main()

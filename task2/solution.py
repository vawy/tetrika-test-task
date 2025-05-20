import requests
from bs4 import BeautifulSoup
import csv


def get_animals_count():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    letter_counts = {}

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        category_block = soup.find('div', class_='mw-category-columns')
        if not category_block:
            break

        category_groups = category_block.find_all('div', class_='mw-category-group')

        for group in category_groups:
            letter = group.find('h3').text.strip()
            if not letter.isalpha():
                continue

            items = group.find_all('li')
            count = len(items)

            if letter in letter_counts:
                letter_counts[letter] += count
            else:
                letter_counts[letter] = count

        next_page = soup.find('a', string='Следующая страница')
        if not next_page:
            break

        url = "https://ru.wikipedia.org" + next_page['href']

    return letter_counts


def save_to_csv(counts, filename='beasts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])


if __name__ == '__main__':
    counts = get_animals_count()
    save_to_csv(counts)
    print("Данные сохранены в beasts.csv")
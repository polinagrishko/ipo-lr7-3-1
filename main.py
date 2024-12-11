books = [
    {"title":"Норвежский лес","author":"Харуки Мураками","year":1987}, # словарь для книги 1 с ключами title, author, year
    {"title": "Хроники заводной птицы", "author": "Харуки Мураками", "year":1994 },# словарь для книги 2 с ключами title, author, year
    {"title": "Фауст", "author":"Иоганн Вольфганг фон Гёте", "year": 1808}, # словарь для книги 3 с ключами title, author, year
    {"title": "Спеши Любить", "author":"Николас Спаркс", "year":1999 },# словарь для книги 4 с ключами title, author, year
    {"title": "Гордость и Предубеждение", "author": "Джейн Остин", "year":1813 }# словарь для книги 5 с ключами title, author, year
]
# Цикл вывода информации о книгах 
count = 1 # инициализация переменной для вывода номера книги
for book in books: # цикл, перебиращий каждый словарь book в списке books
    print(f"---------------------- Книга {count} ----------------------") #форматированная строка с выводом номера книги
    print(f"Название: {book["title"]}, Автор: {book["author"]}")# вывод назваания и автора
    print(f"----------------------{book["year"]}----------------------") # выывод года издания
    print(" ")# отступ между каждой книгой
    count+=1 # увеличение переменной номера книг на 1
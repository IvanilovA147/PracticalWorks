import sqlite3

def create_database():
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Articles (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL,
                            author TEXT NOT NULL
                        )''')
        conn.commit()

def add_article():
    title = input("Введіть заголовок статті: ")
    content = input("Введіть текст статті: ")
    author = input("Введіть ім'я автора: ")
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Articles (title, content, author) VALUES (?, ?, ?)",
                       (title, content, author))
        conn.commit()
        print(f"Стаття '{title}' додана успішно.")

def delete_article():
    article_id = input("Введіть ID статті для видалення: ")
    if not article_id.isdigit():
        print("Помилка: ID має бути числом!")
        return
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Articles WHERE id = ?", (article_id,))
        if cursor.rowcount:
            print(f"Стаття з ID {article_id} видалена.")
        else:
            print("Помилка: За таким ID нічого нема")
        conn.commit()

def view_articles():
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content, author FROM Articles")
        articles = cursor.fetchall()
        if articles:
            for article in articles:
                article_id, title, content, author = article
                print(f"ID: {article_id}\nЗаголовок: {title}\nВміст:\n{content}\nАвтор: {author}")
                print("=" * 40)
        else:
            print("В базі даних нічого нема")

def view_article_by_id():
    article_id = input("Введіть ID статті для перегляду: ")
    if not article_id.isdigit():
        print("Помилка: ID має бути числом!")
        return
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, content, author FROM Articles WHERE id = ?", (article_id,))
        article = cursor.fetchone()
        if article:
            title, content, author = article
            print(f"Заголовок: {title}\nВміст:\n{content}\nАвтор: {author}")
        else:
            print("Стаття не знайдена.")

def main():
    while True:
        print("Меню:")
        print("1. Додати статтю")
        print("2. Видалити статтю")
        print("3. Переглянути всі статті")
        print("4. Переглянути статтю за ID")
        print("5. Вийти")
        choice = input("Виберіть дію: ")
        if choice == "1":
            add_article()
        elif choice == "2":
            delete_article()
        elif choice == "3":
            view_articles()
        elif choice == "4":
            view_article_by_id()
        elif choice == "5":
            print("Вихід...")
            break
        else:
            print("Помилка: неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()

import sqlite3

def CREATE():
    conn = sqlite3.connect("Стаття")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        заголовок TEXT NOT NULL,
                        content TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_article(title, content):
    """Додає нову статтю до бази даних."""
    conn = sqlite3.connect("Стаття")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO articles (заголовок, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

def delete_article(article_id):
    """Видаляє статтю за її ID."""
    conn = sqlite3.connect("Стаття")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()

def get_article(article_id):
    """Повертає вміст статті за її ID."""
    conn = sqlite3.connect("Стаття")
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()
    conn.close()
    return article if article else "Стаття не знайдена"

# Тестування функцій
if __name__ == "__main__":
    CREATE()
    add_article("Перша стаття", "Це тестовий вміст першої статті.")
    print(get_article(1))
    delete_article(1)
    print(get_article(1))
import pandas as pd
import matplotlib.pyplot as plt

# 1. Читаємо CSV файл
df = pd.read_csv('bestsellers with categories.csv')

# 2. Виводимо перші 5 рядків
print("Перші 5 рядків таблиці:")
print(df.head())

# 3. Визначаємо розміри датасету
rows, cols = df.shape
print(f"Розмір датасету: Кількість рядків: {rows}, Кількість стовпців: {cols}")
print("Відповідь: Про скільки книг зберігає дані датасет?")
print(f"Відповідь: Датасет зберігає дані про {rows} книг.")

# 4. Змінюємо назви колонок
df.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']
print("Таблиця після зміни назв колонок:")
print(df.head())

# 5. Перевіряємо пропуски
missing_values = df.isna().sum()
print("Кількість пропусків у кожній колонці:")
print(missing_values)
print("Відповідь: Чи є в якихось змінних пропуски? (Так / ні)")
print("Відповідь: Ні.")

# 6. Унікальні жанри
unique_genres = df['genre'].unique()
print("Унікальні жанри:")
print(unique_genres)
print("Відповідь: Які є унікальні жанри?")
print(f"Відповідь: Унікальні жанри: {', '.join(unique_genres)}.")

# 7. Діаграма розподілу цін
df['price'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Ціна (долари)')
plt.ylabel('Кількість книг')
plt.title('Розподіл цін книг')
plt.show()

# 8. Статистики для ціни
max_price = df['price'].max()
min_price = df['price'].min()
mean_price = df['price'].mean()
median_price = df['price'].median()
print(f"Максимальна ціна: {max_price}")
print(f"Мінімальна ціна: {min_price}")
print(f"Середня ціна: {mean_price}")
print(f"Медіанна ціна: {median_price}")
print("Відповідь: Максимальна ціна?")
print(f"Відповідь: {max_price} доларів.")
print("Відповідь: Мінімальна ціна?")
print(f"Відповідь: {min_price} доларів.")
print("Відповідь: Середня ціна?")
print(f"Відповідь: {mean_price} доларів.")
print("Відповідь: Медіанна ціна?")
print(f"Відповідь: {median_price} доларів.")

# 9. Найвищий рейтинг
max_rating = df['user_rating'].max()
print(f"Найвищий рейтинг: {max_rating}")
print("Відповідь: Який рейтинг у датасеті найвищий?")
print(f"Відповідь: {max_rating}.")

# 10. Кількість книг із найвищим рейтингом
num_max_rating = len(df[df['user_rating'] == max_rating])
print(f"Кількість книг із рейтингом {max_rating}: {num_max_rating}")
print("Відповідь: Скільки книг мають такий рейтинг?")
print(f"Відповідь: {num_max_rating} книги.")

# 11. Книга з найбільшою кількістю відгуків
most_reviews_book = df.loc[df['reviews'].idxmax(), 'name']
max_reviews = df['reviews'].max()
print(f"Книга з найбільшою кількістю відгуків: {most_reviews_book}, відгуків: {max_reviews}")
print("Відповідь: Яка книга має найбільше відгуків?")
print(f"Відповідь: {most_reviews_book}.")

# 12. Найдорожча книга 2015 року
df_2015 = df[df['year'] == 2015]
most_expensive_2015 = df_2015.loc[df_2015['price'].idxmax(), 'name']
max_price_2015 = df_2015['price'].max()
print(f"Найдорожча книга 2015 року: {most_expensive_2015}, ціна: {max_price_2015}")
print("Відповідь: З тих книг, що потрапили до Топ-50 у 2015 році, яка книга найдорожча?")
print(f"Відповідь: {most_expensive_2015}.")

# 13. Кількість книг жанру Fiction у 2010 році
fiction_2010 = len(df[(df['genre'] == 'Fiction') & (df['year'] == 2010)])
print(f"Кількість книг жанру Fiction у 2010 році: {fiction_2010}")
print("Відповідь: Скільки книг жанру Fiction потрапили до Топ-50 у 2010 році?")
print(f"Відповідь: {fiction_2010} книг.")

# 14. Кількість книг із рейтингом 4.9 у 2010 та 2011 роках
rating_4_9_2010_2011 = len(df[(df['user_rating'] == 4.9) & (df['year'].isin([2010, 2011]))])
print(f"Кількість книг із рейтингом 4.9 у 2010 та 2011 роках: {rating_4_9_2010_2011}")
print("Відповідь: Скільки книг з рейтингом 4.9 потрапило до рейтингу у 2010 та 2011 роках?")
print(f"Відповідь: {rating_4_9_2010_2011} книга.")

# 15. Сортування книг 2015 року дешевше 8 доларів
cheap_2015 = df[(df['year'] == 2015) & (df['price'] < 8)].sort_values(by='price')
print("Відсортовані книги 2015 року дешевше 8 доларів:")
print(cheap_2015)
last_book = cheap_2015.iloc[-1]['name']
print("Відповідь: Яка книга остання у відсортованому списку?")
print(f"Відповідь: {last_book}.")

# 16. Мінімальні та максимальні ціни за жанрами
genre_price_stats = df.groupby('genre')['price'].agg(['min', 'max'])
print("Мінімальні та максимальні ціни за жанрами:")
print(genre_price_stats)
print("Відповідь: Максимальна ціна для жанру Fiction?")
print(f"Відповідь: {genre_price_stats.loc['Fiction', 'max']} доларів.")
print("Відповідь: Мінімальна ціна для жанру Fiction?")
print(f"Відповідь: {genre_price_stats.loc['Fiction', 'min']} доларів.")
print("Відповідь: Максимальна ціна для жанру Non Fiction?")
print(f"Відповідь: {genre_price_stats.loc['Non Fiction', 'max']} доларів.")
print("Відповідь: Мінімальна ціна для жанру Non Fiction?")
print(f"Відповідь: {genre_price_stats.loc['Non Fiction', 'min']} доларів.")

# 17. Кількість книг для кожного автора
author_books = df.groupby('author').agg({'name': 'count'}).reset_index()
author_books.columns = ['author', 'book_count']
print("Кількість книг для кожного автора:")
print(author_books.head())
rows_author, cols_author = author_books.shape
print(f"Розмірність таблиці: {rows_author} рядків, {cols_author} стовпців")
print("Відповідь: Якої розмірності вийшла таблиця?")
print(f"Відповідь: {rows_author} рядків, {cols_author} стовпців.")
max_books_author = author_books.loc[author_books['book_count'].idxmax()]
print("Відповідь: Який автор має найбільше книг?")
print(f"Відповідь: {max_books_author['author']}.")
print("Відповідь: Скільки книг цього автора?")
print(f"Відповідь: {max_books_author['book_count']} книг.")

# 18. Середній рейтинг для кожного автора
author_rating = df.groupby('author').agg({'user_rating': 'mean'}).reset_index()
author_rating.columns = ['author', 'avg_rating']
print("Середній рейтинг для кожного автора:")
print(author_rating.head())
min_rating_author = author_rating.loc[author_rating['avg_rating'].idxmin()]
print("Відповідь: У якого автора середній рейтинг мінімальний?")
print(f"Відповідь: {min_rating_author['author']}.")
print("Відповідь: Який у цього автора середній рейтинг?")
print(f"Відповідь: {min_rating_author['avg_rating']}.")

# 19. З’єднання та сортування
combined_df = pd.concat([author_books.set_index('author'), author_rating.set_index('author')], axis=1).reset_index()
combined_df = combined_df.sort_values(by=['book_count', 'avg_rating'], ascending=[True, True])
print("З’єднана та відсортована таблиця:")
print(combined_df.head())
first_author = combined_df.iloc[0]['author']
print("Відповідь: Який автор перший у списку?")
print(f"Відповідь: {first_author}.")

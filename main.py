import sqlite3

# 새로운 연결을 설정하고 모든 테이블을 다시 생성하기
conn = sqlite3.connect(r'C:\Users\82102\Desktop\파이썬\TEST_2024-03-07_DB\movies.db')
c = conn.cursor()

# 첫 번째 테이블 (movies_info) 생성
c.execute('''
CREATE TABLE IF NOT EXISTS movies_info
(title TEXT, description TEXT, rating INTEGER, notes TEXT)
''')

# 두 번째 테이블 (movies_categories) 생성
c.execute('''
CREATE TABLE IF NOT EXISTS movies_categories
(title TEXT, category TEXT)
''')

# 세 번째 테이블 (movies_actors) 생성
c.execute('''
CREATE TABLE IF NOT EXISTS movies_actors
(title TEXT, actor TEXT)
''')

# movies_info 테이블에 초기 데이터 삽입
movies_info_data = [
    ('Inception', 'A thief who steals corporate secrets through use of dream-sharing technology.', 5, 'Must watch'),
    ('The Matrix', 'A computer hacker learns about the true nature of reality and his role in the war against its controllers.', 5, 'Classic'),
    ('Interstellar', 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.', 5, 'Thought-provoking')
]
c.executemany('INSERT INTO movies_info (title, description, rating, notes) VALUES (?, ?, ?, ?)', movies_info_data)

# movies_categories 테이블에 초기 데이터 삽입
movies_categories_data = [
    ('Inception', 'Sci-Fi'),
    ('The Matrix', 'Sci-Fi'),
    ('Interstellar', 'Sci-Fi'),
    ('Inception', 'Sci-Fi'),  # 중복된 항목으로 다시 추가
    ('Inception', 'Thriller'),
    ('Inception', 'Horror')
]
c.executemany('INSERT INTO movies_categories (title, category) VALUES (?, ?)', movies_categories_data)

# movies_actors 테이블에 초기 데이터 삽입
movies_actors_data = [
    ('Inception', 'Leonardo DiCaprio'),
    ('The Matrix', 'Keanu Reeves'),
    ('Interstellar', 'Matthew McConaughey')
]
c.executemany('INSERT INTO movies_actors (title, actor) VALUES (?, ?)', movies_actors_data)

# 변경사항 커밋
conn.commit()

# 데이터 조인하여 조회
c.execute('''
SELECT mi.title, mi.description, mi.rating, mi.notes, GROUP_CONCAT(mc.category, ', ') AS categories, ma.actor
FROM movies_info mi
LEFT JOIN movies_categories mc ON mi.title = mc.title
LEFT JOIN movies_actors ma ON mi.title = ma.title
GROUP BY mi.title
''')

# 조인된 데이터 출력을 위해 가져오기
joined_data = c.fetchall()

# 연결 종료
conn.close()

joined_data
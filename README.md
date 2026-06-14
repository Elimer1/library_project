## **LIBRARY PROJECT**

this is a library manager project
the project works with data sets for the books in the library and the members of the libary
the user can either perfrom CRUD operations or read data on the books and the members

## **DOCKER RUN CODE**

docker run --name library_mysql_server -e MYSQL_ROOT_PASSWORD=your_password -p 3307:3306 -d mysql:latest

**FILE STRUCTURE**:
library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore

**TABLES STRUCTURE**

## book table

| שדה                   | הסבר                                                                                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                    | מפתח ראשי                                                                                                                                            |
| title                 | כותרת הספר, עמודה לא ריקה, הקיימות 50 תווים חוזים                                                                                                    |
| author                | שם המחבר, עמודה לא ריקה, הקיימות 50 תווים חוזים                                                                                                      |
| genre                 | ערכי genre מחוברים: Fiction \| Non-Fiction \| Science \| History \| Other — מוש כלי ערך אחד מחברי ENUM בטמונן, כל ערך אחד מחברי שניהו, עמודה לא ריקה |
| is_available          | האם הספר זמין להשאלה — FALSE ללא שאלה, עמודה לא ריקה                                                                                                 |
| borrowed_by_member_id | מזהה חבר שמחזיק את הספר — NULL אם זמין                                                                                                               |

## member table

| שדה           | הסבר                                                |
| ------------- | --------------------------------------------------- |
| id            | מפתח ראשי                                           |
| name          | שם החבר, עמודה לא ריקה, הקיימות 50 תווים חוזים      |
| email         | כתובת מייל - ייחודי, עמודה לא ריקה                  |
| is_active     | האם החבר פעיל — FALSE לא לשאול עמודה לא ריקה        |
| total_borrows | מונה סה"כ השאלות — ערך 1-0 בכלל השאלה עמודה לא ריקה |

## **SYSTEM RULES**

| חוק | נושא          | הכלל                                                                                                   |
| --- | ------------- | ------------------------------------------------------------------------------------------------------ |
| 1   | יצירת ספר     | השתמשו בשדות title/author/genre השדה is_available=True, borrowed_by=NULL                               |
| 2   | genre         | חייב להיות Fiction / Non-Fiction / Science / History / Other — כל ערך כמו לאחור (POST) ו-PATCH (PATCH) |
| 3   | יצירת חבר     | השתמשו בשדות name/email השדה is_active=True, total_borrows=0                                           |
| 4   | email         | חייב להיות ייחודי — אם קיים כבר חבר מחברים שיראה                                                       |
| 5   | חבר לא פעיל   | אם is_active=False אי אפשר להשאיל ספר                                                                  |
| 6   | ספר לא זמין   | אי אפשר להשאיל ספר שכבר משוכר (is_available=False)                                                     |
| 7   | מקסימום ספרים | חבר לא יכול להחזיק יותר 3-ב ספרים בו-זמנית                                                             |
| 8   | החזרות ספר    | ניתן להחזיר ספר רק אם הוא משוכר לאותו חבר שמחזירו אותו                                                 |

## **ENDPOINTS**

## Books

| Method | Endpoint                       | תיאור          |
| ------ | ------------------------------ | -------------- |
| POST   | /books                         | יצירת ספר      |
| GET    | /books                         | כל הספרים      |
| GET    | /books/{id}                    | ספר לפי ID     |
| PATCH  | /books/{id}                    | עדכון ספר      |
| PATCH  | /books/{id}/borrow/{member_id} | השאלת ספר לחבר |
| PATCH  | /books/{id}/return/{member_id} | החזרת ספר מחבר |

## Members

| Method | Endpoint                 | תיאור      |
| ------ | ------------------------ | ---------- |
| POST   | /members                 | יצירת חבר  |
| GET    | /members                 | כל החברים  |
| GET    | /members/{id}            | חבר לפי ID |
| PATCH  | /members/{id}            | עדכון חבר  |
| PATCH  | /members/{id}/deactivate | השבתת חבר  |
| PATCH  | /members/{id}/activate   | הפעלת חבר  |

## Reports

| Method | Endpoint                | תיאור           |
| ------ | ----------------------- | --------------- |
| GET    | /reports/summary        | דוח כללי        |
| GET    | /reports/books-by-genre | ספרים לפי ז'אנר |
| GET    | /reports/top-member     | החבר הכי פעיל   |

user selects either a crud operation or to read data

from phonygres import execute_sql, Database

def test_empty_create(db: Database):
    execute_sql(db, '''
    CREATE TABLE empty();
    ''')

def test_basic_create(db: Database):
    execute_sql(db, '''
    CREATE TABLE basic(
        num INT,
        field CHARACTER VARYING
    );
    ''')

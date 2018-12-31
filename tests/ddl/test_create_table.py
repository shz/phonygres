from phonygres import Database

def test_empty_create(db: Database):
    db.execute('''
    CREATE TABLE empty();
    ''')

def test_basic_create(db: Database):
    db.execute('''
    CREATE TABLE basic(
        num INT,
        field CHARACTER VARYING
    );
    ''')

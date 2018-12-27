def test_empty_create(db):
    db.execute('''
    CREATE TABLE empty();
    ''')

def test_basic_create(db):
    db.execute('''
    CREATE TABLE basic(
        id SERIAL,
        field CHARACTER VARYING
    );
    ''')

def test_empty_create(db):
    db.execute('''
    CREATE TABLE test();
    ''')

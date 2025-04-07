import pytest
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker

db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
db = create_engine(db_connection_string)
Session = sessionmaker(bind=db)

@pytest.fixture
def db_session():
    connection = db.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

def test_db_connection(db_session):
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'teacher' in names

def test_insert(db_session):
    sql = text('INSERT INTO teacher (teacher_id, email, group_id) VALUES (:teacher_id, :email, :group_id)')
    db_session.execute(sql, {'teacher_id': 25, 'email': 'fruktaym@gmail.com', 'group_id': 15})
    db_session.commit()

    result = db_session.execute(text("SELECT * FROM teacher WHERE teacher_id = :teacher_id"), {'teacher_id': 25})
    row = result.fetchall()
    assert row is not None
    assert row [0][1] == 'fruktaym@gmail.com'

def test_update(db_session):
    db_session.execute(text('INSERT INTO teacher (teacher_id, email, group_id) VALUES (:teacher_id, :email, :group_id)'),
                       {'teacher_id': 25, 'email': 'fruktaym@gmail.com', 'group_id': 15})
    db_session.commit()

    sql = text("UPDATE teacher SET group_id = :group_id WHERE teacher_id = :teacher_id")
    db_session.execute(sql, {'group_id': 95, 'teacher_id': 25})
    db_session.commit()

    result = db_session.execute(text("SELECT group_id FROM teacher WHERE teacher_id = :teacher_id"), {'teacher_id': 25})
    row = result.fetchall()
    assert row[0][0] == 95

def test_delete(db_session):
    db_session.execute(text('INSERT INTO teacher (teacher_id, email, group_id) VALUES (:teacher_id, :email, :group_id)'),
                       {'teacher_id': 25, 'email': 'fruktaym@gmail.com', 'group_id': 15})
    db_session.commit()

    sql = text("DELETE FROM teacher WHERE teacher_id = :teacher_id")
    db_session.execute(sql, {"teacher_id": 25})
    db_session.commit()

    result = db_session.execute(text("SELECT * FROM teacher WHERE teacher_id = :teacher_id"), {'teacher_id': 25})
    row = result.fetchone()
    assert row is None
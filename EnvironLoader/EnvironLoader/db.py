""" DB Commands """

from contextlib import contextmanager
import os
import re
import sqlite3

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB_NAME = 'envloader.db'
DB_PATH = os.path.join(BASE_DIR, DB_NAME)

def create_db():
    """ Create DB """
    open(DB_PATH, 'a').close()
    print "DB created at {}".format(DB_PATH)


def create_tables():
    """ Create all tables """
    with _connection() as conn:
        conn.execute("""CREATE TABLE envvars(
                            key varchar(100),
                            val varchar(100),
                            description varchar(100)
                        )
                     """)


def insert_env_var(key, val, description):
    """ Insert environment variable """
    with _connection() as conn:
        command = """INSERT INTO envvars VALUES ('{key}', '{val}', '{description}')"""
        conn.execute(command.format(key=key, val=val, description=description))
        conn.commit()


def search_env_vars(search_str):
    """ Search env vars for search_str """
    operands = [None] + re.findall(r'[\&\|]', search_str)
    search_terms = [term.strip() for term in re.split(r'[\&\|]', search_str)]
    command = 'SELECT * from envvars WHERE '
    for term, operand in zip(search_terms, operands):
        if operand == '&':
            command += 'AND '
        elif operand == '|':
            command += 'OR '
        command += '('
        for idx, col in enumerate(['key', 'val', 'description']):
            command += "{} LIKE '%{}%' ".format(col, term)
            if idx < 2:
                command += 'OR '
        command += ') '
    with _connection() as conn:
        curs = conn.execute(command)
        return [{'key': rec[0], 'val': rec[1], 'description': rec[2]}
                for rec in curs.fetchall()]


@contextmanager
def _connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
        conn.close()
    except sqlite3.OperationalError:
        print "ERROR: DB error, try running `envloader init`"
        exit(1)

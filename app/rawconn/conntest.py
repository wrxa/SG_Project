import sqlalchemy


def main():
    engine = sqlalchemy.create_engine("postgresql://postgres:postgres@192.168.33.110:5432/energy_island", encoding="utf-8", echo=True)
    conn = engine.connect()
    s = sqlalchemy.sql.text("SELECT col_description(a.attrelid, a.attnum) AS comment, a.attname AS name \
    FROM pg_class AS c,pg_attribute AS a \
    WHERE c.relname = 'ccpp_ccpp' AND a.attrelid = c.oid AND a.attnum>0")
    print conn.execute(s, id=3).fetchall()
    conn.close()


if __name__ == '__main__':
    main()


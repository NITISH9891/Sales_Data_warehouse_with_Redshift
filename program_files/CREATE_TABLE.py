import configparser
# import psycopg2
import redshift_connector
from SQL_DATA import drop_table_queries, create_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('cluster.cfg')

    conn = redshift_connector.connect("host='{}', database='{}', user='{}', password='{}', port={}").format(*config['CLUSTER'].values())
    
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    
    conn.close()


if __name__ == "__main__":
    main()
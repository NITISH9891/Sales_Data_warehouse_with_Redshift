import configparser
import redshift_connector
from SQL_DATA import copy_table_queries


def load_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('cluster.cfg')

    conn = redshift_connector.connect("host='{}', database='{}', user='{}', password='{}', port={}").format(*config['CLUSTER'].values())

    cur = conn.cursor()
    
    load_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
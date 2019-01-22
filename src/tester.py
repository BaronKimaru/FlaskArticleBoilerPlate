from pprint import pprint
import psycopg2


def tester():
    conn = psycopg2.connect("dbname = miner_dev password = 5cR)4{>t host = 35.189.241.51 user = ian_kimaru port = 5432")
    if conn:
        pprint("success")

if __name__ == "__main__":
    tester()

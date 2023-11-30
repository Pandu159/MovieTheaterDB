# import library for postgreSQL connection
import psycopg2


# connect to database server
conn = psycopg2.connect(host="localhost", dbname="JarMovies", user="postgres", password="database_design", port=5433)
# create cursor to database
cur = conn.cursor()

########################################################################################################################

# initiate tables in database if they don't exist
cur.execute(open("Tables.sql", "r").read())
conn.commit()


# insert into or update values in database
cur.execute(open("Inserts.sql", "r").read())
conn.commit()


print("CREATE-INSERT complete")

########################################################################################################################
# close cursor and database connection
cur.close()
conn.close()



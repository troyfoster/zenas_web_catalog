import streamlit
import snowflake.connector

streamlit.title('My Parents\' New Healthy Diner')

my_conx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select current_user(), current_account(), current_region()")
my_data_row = my_cur.fetchone()
streamlit.text("Hellow from Snowflake:")
streamlit.text(my_data_row)



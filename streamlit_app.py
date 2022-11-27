import streamlit
import requests
import pandas as pd
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized 

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boild Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')

streamlit.header('🍌🍓 Build Your Own Fruit Smoothie 🥝🍇')

df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df_list = df.set_index('Fruit')
df_selected = streamlit.multiselect('Pick Some Fruits:', list(df_list.index),['Avocado', 'Strawberries'])
df_show = df_list.loc[df_selected]

streamlit.dataframe(df_show)

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_func = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_func)

except URLError as e:
  streamlit.error()
streamlit.stop()


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_row)

#Allow enduser to select fruit
add_fruit = streamlit.text_input('What fruit would you like to add','Kiwi')
streamlit.write('The user entered ', add_fruit)


my_cur.execute("insert into fruitlist values ('from streamlit')")

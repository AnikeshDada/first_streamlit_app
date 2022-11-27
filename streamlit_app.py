import streamlit
import requests
import pandas as pd
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized 

def get_fruit_load_list():
  streamlit.text("In fruit load list :)")
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.FRUIT_LOAD_LIST")
    return my_cur.fetchall()

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

streamlit.header("The Fruit Load List Contains:")

#Add a Buttion to load fruits
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into pc_rivery_db.public.FRUIT_LOAD_LIST values ('"+ new_Fruit +"')")
    return "Thanks for adding " + new_fruit

add_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add fruit to list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_fruit)
  streamlit.text(back_from_function)
  

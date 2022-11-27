import streamlit

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boild Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')

streamlit.header('🍌🍓 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df_list = df.set_index('Fruit')
df_selected = streamlit.multiselect('Pick Some Fruits:', list(df_list.index),['Avocado', 'Strawberries'])
df_show = df_list.loc[df_selected]

streamlit.dataframe(df_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

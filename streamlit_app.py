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
streamlit.multiselect('Pick Some Fruits:', list(df_list.index))
streamlit.dataframe(df_list)

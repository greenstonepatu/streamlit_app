import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError


streamlit.title('🥝Zdrowe Śniadanie🍇')
streamlit.text('🍞Omega3 i Owśianka z jagodami')
streamlit.text('🥗Jabłka, Banany, Gruszki')
streamlit.header('🥭Zbuduj swój własny owocowy koktajl')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = myfruit_list_set_indekx('Fruit')

fruits_selected = streamlit.multiselect("Wybierz owoce:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected])
streamlit_dataframe(fruits_to_show)

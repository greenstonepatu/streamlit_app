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
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Wybierz owoce:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Owocowe informacje")
try:
  fruit_choice = streamlit.text_input('Informacje o jakim owocu potrzebuesz?')
  if not fruit_choice:
    streamlit.error("Proszę wybierz jakiś owoc")
  else:
    back_from_get_fruityvice_data = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_get_fruityvice_data)
except URLError as e:
 streamlit.error()

streamlit.header("Lista owoców zawiera:")
def get_fruit_load_list():
  with my_cnx_cursor() as my_cur:
    my_cur.execute("select * from FRUIT_LOAD_LIST")
    return my_curr_fetchall()
  
  
if streamlit.button('Wyświetl Liste Owoców'):
  my_cnx = snowflake.connector.connect(**streamlit_secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)





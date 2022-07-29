import streamlit
import pandas

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text('Omega 3 blueberry oatmeal')
streamlit.text('Kale, spinach and rocket smoothie')
streamlit.text('Hard-Boiled free range egg')

streamlit.header('Build your own fruit smoothie')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

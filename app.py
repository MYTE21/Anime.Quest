import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://ml557:hhDyMRdbvUMD6cGz@anime-quest.yomhl8y.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client["anime_quest"]
collection = db["anime_country"]

countries = collection.find()

for country in countries:
    st.write(country["Country"])

st.write("DONE..!")

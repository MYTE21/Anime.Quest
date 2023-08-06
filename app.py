import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


username = st.secrets["username"]
password = st.secrets["password"]
cluster_name = st.secrets["cluster_name"]

st.write(username)
st.write(password)
st.write(cluster_name)

# uri = f"mongodb+srv://{username}:{password}@{cluster_name}.yomhl8y.mongodb.net/?retryWrites=true&w=majority"
#
# client = MongoClient(uri, server_api=ServerApi('1'))
#
# db = client["anime_quest"]
# collection = db["anime_country"]
#
# countries = collection.find()
#
# for country in countries[:10]:
#     st.write(country["Country"])

st.write("DONE..!")

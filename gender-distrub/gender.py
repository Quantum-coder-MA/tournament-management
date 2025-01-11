import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


tc = pd.read_excel("tournament_management.xlsx")
table1 = pd.read_excel("tournament_management.xlsx", sheet_name="gender")

def gender_fighter():
    plt.figure(figsize=(18, 10))
    plt.bar(table1["gender"], table1["participant"], color=["blue", "pink"])
    plt.yticks(range(0, table1["participant"].max() + 1, 10), fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlabel("Gender", fontsize=16)
    plt.ylabel("Number of Participants", fontsize=16)
    plt.title("Participants by Gender", fontsize=18, color="red")

    st.pyplot(plt)

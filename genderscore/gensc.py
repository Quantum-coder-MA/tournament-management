import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt 
tc = pd.read_excel("tournament_management.xlsx")
table1 = pd.read_excel("tournament_management.xlsx", sheet_name="genderscore")

def gender_score():
    plt.figure(figsize=(18, 10))

    plt.bar(table1["gender"], table1["totale score"], color=["blue", "pink"])
    plt.yticks(range(0, table1["totale score"].max() + 10, 10), fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlabel("gender", fontsize=16)
    plt.ylabel("total score", fontsize=16)
    plt.title("score by gender", fontsize=18, color="red")
    plt.legend(fontsize=12)
    st.pyplot(plt)
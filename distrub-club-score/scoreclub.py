import streamlit as st
import pandas as pd
from openpyxl import Workbook
import matplotlib.pyplot as plt

sc = pd.read_excel("tournament_management.xlsx")
table1 = pd.read_excel("tournament_management.xlsx", sheet_name="scoreclub")
def score_destrub():
    plt.figure(figsize=(18, 10))
    x_positions = range(len(table1["club"]))  

    plt.bar([x - 0.4 for x in x_positions], table1["totle-score"], width=0.2, label="score", color="red")
    plt.bar([x - 0.2 for x in x_positions], table1["totale-time"], width=0.2, label="time", color="blue")
    plt.bar(x_positions, table1["bronze"], width=0.2, label="bronze", color="#cd7f32")
    plt.bar([x + 0.2 for x in x_positions], table1["silver"], width=0.2, label="silver", color="silver")
    plt.bar([x + 0.4 for x in x_positions], table1["gold"], width=0.2, label="gold", color="gold")

    plt.xticks(x_positions, table1["club"], rotation=45, fontsize=12)
    plt.legend(fontsize=12)
    plt.title("Fighter Performance by Club", fontsize=16)
    plt.xlabel("Club", fontsize=14)
    plt.ylabel("Metrics", fontsize=14)

    st.pyplot(plt)
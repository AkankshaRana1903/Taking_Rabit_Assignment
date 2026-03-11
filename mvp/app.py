import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt AI 🐰")
st.write("Ask questions about your business data")

uploaded_file = st.file_uploader("Upload Sales CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.write(df)

    question = st.text_input("Ask a question")

    if question:

        if "revenue" in question.lower():

            result = df.groupby("Region")["Revenue"].sum()

            st.write("Revenue by Region")
            st.write(result)

            # Direct answer
            max_region = result.idxmax()
            max_value = result.max()
            st.success(f"Highest revenue region: {max_region} ({max_value})")

            # Chart
            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)

            ax.set_title("Revenue by Region")
            ax.set_xlabel("Region")
            ax.set_ylabel("Revenue")

            st.pyplot(fig)

        else:
            st.write("Try asking about revenue or region.")
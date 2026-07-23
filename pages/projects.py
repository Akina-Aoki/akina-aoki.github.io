import streamlit as st


st.title("🛠️ Projects")

st.write(
    """
    This is where I will present the data engineering projects I have built,
    including the problem, architecture, technology stack, implementation,
    challenges, and final results.
    """
)

st.markdown("### Projects coming soon")

project_one, project_two = st.columns(2)

with project_one:
    with st.container(border=True):
        st.subheader("📈 Finnhub Modern Data Stack")
        st.write(
            "An end-to-end stock market data pipeline using Kafka, Amazon S3, "
            "Airflow, dbt, PostgreSQL/TimescaleDB, Docker, and Terraform."
        )

with project_two:
    with st.container(border=True):
        st.subheader("🏃 Marathos Atlas")
        st.write(
            "A Databricks medallion architecture project built from more than "
            "seven million ultramarathon records."
        )
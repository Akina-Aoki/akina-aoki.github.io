from pathlib import Path
import streamlit as st

# =========================================================
# Project paths & Assets
# =========================================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROFILE_IMAGE = PROJECT_ROOT / "assets" / "profile_pic.jpg"
RESUME_FILE = PROJECT_ROOT / "assets" / "CV_Aira_Franco_en.pdf" 

# =========================================================
# Header Section
# =========================================================
col1, col2 = st.columns([1, 2.5], gap="medium")

with col1:
    if PROFILE_IMAGE.exists():
        st.image(str(PROFILE_IMAGE), width=230)
    else:
        st.warning("Profile picture not found. Place it in `assets/profile_pic.jpg`.")

with col2:
    st.title("Aira Franco")
    st.write(
        "Aspiring Data Engineer \n\n"
        "An aspiring Data Engineering experienced in architecting the full data pipelines and platforms that transform raw data into reliable, tested analytics-ready data for stakeholders. "
        "Experienced in designing pipelines, modelling data, and enabling business decision-making through scalable data solutions. "
        "Adaptable to new tools, environments, and domain-specific data ecosystems."
        ""
        "*I have permanent work authorization in Sweden (no sponsorship required."
    )
    
    # Resume Download Button
    if RESUME_FILE.exists():
        with open(RESUME_FILE, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=pdf_bytes,
            file_name="CV_Aira_Franco_en.pdf",
            mime="application/pdf",
        )
    else:
        st.download_button(
            label="📄 Download Resume",
            data="Currently unavailable",
            file_name="resume_placeholder.txt",
            disabled=True,
            help="Add CV_Aira_Franco_en.pdf to the assets folder to enable."
        )

    st.write("📫 adelosofranco@gmail.com | 📞 +46 70 566 6295")
    st.write("📍 Solursgränd 9, 162 65, Vällingby")

# =========================================================
# Social Links Section
# =========================================================
st.write("\n")
links_cols = st.columns(4)
links_cols[0].write("[YouTube](https://www.youtube.com/@Aira_Data_Engineering)")
links_cols[1].write("[LinkedIn](https://www.linkedin.com/in/aira-franco0965/)")
links_cols[2].write("[GitHub](https://github.com/Akina-Aoki)")
links_cols[3].write("[Projects Blog](https://hashnode.com/@Aira)")

# =========================================================
# Education & Authorizations
# =========================================================
st.write("\n")
st.subheader("Education & Profile")
st.write(
    """
    - 🎓 **Data Engineering**, Stockholms Tekniska Institut (September 2025 - May 2027)
    - 🎓 **English Literature**, Hokusei Gakuen University (April 2015 - March 2017)

    """
)

# =========================================================
# Hard Skills
# =========================================================
st.write("\n")
st.subheader("Technical Skills")
st.write(
    """
    - 👩‍💻 **Programming:** Python (Functional and OOP), Jupyter Notebook, Pandas (EDA, Data Cleaning, Transformation, Analysis), FastAPI (RestAPI, CRUD), Pydantic (Data Validation)
    - 🗄️ **Database:** SQL, DuckDB (OLAP), Postgres (OLTP), PGAdmin4, Data Modelling (Conceptual - Logical Physical, Normalization)
    - ☁️ **Cloud and Containerization:** Azure, Databricks, Terraform (Infrastructure as Code), Docker
    - ⚙️ **Data Pipelines:** ELT/ETL, Kafka (Batch and Streaming Data), Snowflake (Data Warehousing), DLT (Hub EL), Dagster (Orchestration), DBT (Transformation), Dimensional Modelling
    - 🔄 **CI/CD:** Github Actions, Git, Bash, Pytest
    - 📊 **Visualization:** Evidence Dashboard, Streamlit, Matplotlib, PowerBI, Grafana
    - 🤖 **AI Engineering (Upcoming Fall 2026):** AI Agents in daily workflow, LLM Ops, ML FLow (Monitoring, Tracing, Governance, Evaluate) RAGs, Vector Database
    """
)

# =========================================================
# Work History
# =========================================================
st.write("\n")
st.subheader("Work History")
st.write("---")

# Job 1
st.write("🚧 **Operations Assistant | Inditex**")
st.write("2020 - present")
st.write("Stockholm, Sweden")

st.write(
    """
    - Optimized inventory and logistics workflows across departments, improving product distribution efficiency under strict operational timelines.
    - Developed a strong understanding of stock movement, demand patterns, and operational bottlenecks, directly informing my transition into data engineering for inventory and analytics systems.
    - **Skills:** Inventory Management, Retail Operations
    """
)
st.write("\n")

# Job 2
st.write("🚧 **English Language Teacher | Self-employed**")
st.write("2015 - 2019")
st.write("Sapporo, Japan")

st.write(
    """
    - Founded and operated an English tutoring business alongside university studies, delivering one-on-one and group lessons for children and adults with a focus on conversation, grammar, and university exam readiness.
    - **Skills:** Language Teaching, Lesson Planning
    """
)
st.write("\n")


# Job 3
st.write("🚧 **Translator (Japanese ↔ English) | Self-employed**")
st.write("2015 - 2019")
st.write("Sapporo, Japan")

st.write(
    """
    - Translated business and general documents between Japanese and English with precision and cultural sensitivity with full ownership of timelines, prioritization, and delivery.
    - Collaborated directly with clients to clarify requirements and align on expectations.
    - **Skills:** Translation
    """
)
st.write("\n")


# Job 4
st.write("🚧 **Hotel Receptionist | The Stay Sapporo Nagomi**")
st.write("2019")
st.write("Sapporo, Japan")

st.write(
    """
    - Handled front-office operations, guest relations, and daily payment reconciliation to ensure efficient service.
    - **Skills:** Administration, Hospitality Service, Booking Systems
    """
)
st.write("\n")



# Job 5
st.write("🚧 **Production Assistant | Krispy Kreme Doughnuts Japan**")
st.write("2018 - 2019")
st.write("Chitose, Japan")

st.write(
    """
    - Assisted in launching food production workflows for the first store in the region, including preparation, handling, and flow coordination.
    - **Skills:** Food Production
    """
)


# Job 6
st.write("🚧 **Bartender | TK6 International Sports Bar**")
st.write("2016 - 2018")
st.write("Sapporo, Japan")

st.write(
    """
    - While studying in university, managed daily bar operations, staff coordination, and cost controls in day-to-day service execution.
    - **Skills:** Restaurant Operations
    """
)
st.write("\n")


# Job 7
st.write("🚧 **Front Desk Assistant | Hilton**")
st.write("2016")
st.write("Sapporo, Japan")

st.write(
    """
    - Coursework and Internship: Balanced reception duties with administrative coordination, helping streamline internal processes and maintain smooth day-to-day operations.
    - **Skills:** Hotel Operations
    """
)
st.write("\n")

# =========================================================
# Projects
# =========================================================
st.write("\n")
st.subheader("Projects")
st.write("---")

# Project 1
st.write("🏆 **Data Platform for Retail Inventory & Sales**")
st.write("*Docker | FastAPI | Kafka | Data Streaming | ETL | Pandas | Pydantic | PostgreSQL | Supabase SQL | DuckDB | Evidence Dashboard*")
st.write(
    """
    - Designed and implemented a data platform integrating APIs, streaming events, and PostgreSQL to provide near real-time visibility into inventory and sales.
    - Enabled tracking of product performance and stock levels, supporting faster operational decisions and reducing risk of stockouts.
    """
)
st.write("\n")

# Project 2
st.write("🏆 **DataOps Pipeline: Validated ETL with PostgreSQL**")
st.write("*SQL | Duck DB | Pandas | Evidence Dashboard*")
st.write(
    """
    - Built a validated ETL pipeline to transform raw CSV data into clean, analytics-ready datasets.
    - Applied data quality rules with Pydantic and Pandas, and loaded both accepted and rejected records into PostgreSQL for transparency and reliable reporting.
    """
)
st.write("\n")

# Project 3
st.write("🏆 **YrkesCo Vocational School Database**")
st.write("*Data Modelling OLTP | PostgreSQL | Docker*")
st.write(
    """
    - ► Built a structured database to organize and manage school data in a clear and reliable way.
    - ► Ensured the data is accurate and consistent, making it easy to use for daily operations and informed decisions.
    """
)
st.write("\n")

# Project 4
st.write("🏆 **Sakila Database Exploratory Data Analysis**")
st.write("*SQL | DuckDB | Pandas | Evidence Dashboard*")
st.write(
    """
    - Explored and analyzed the Sakila dataset using SQL to identify trends, patterns, and key insights.
    - Prepared clean, structured data for dashboards and reporting.
    """
)
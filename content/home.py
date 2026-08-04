"""Data-driven Home page content."""

from types import MappingProxyType


def _immutable_record(**values: object) -> MappingProxyType:
    return MappingProxyType(values)


COMPETENCY_STAGES = (
    _immutable_record(
        number=1,
        title="Programming Foundations",
        skills=(
            "Build applications in Python",
            "Write clean, reusable code",
            "Manage packages and virtual environments",
            "Use testing for reliable results",
        ),
    ),
    _immutable_record(
        number=2,
        title="Query Languages",
        skills=(
            "Use SQL to explore and transform data",
            "Write joins, aggregations, and window functions",
            "Check data quality and accuracy",
            "Support reporting and analysis needs",
        ),
    ),
    _immutable_record(
        number=3,
        title="Data Modeling",
        skills=(
            "Design data structures for different needs",
            "Use normalization and 3NF principles",
            "Work with primary and foreign keys",
            "Understand OLTP vs OLAP use cases",
        ),
    ),
    _immutable_record(
        number=4,
        title="Databases & Storage",
        skills=(
            "Work with PostgreSQL and DuckDB",
            "Design tables, schemas, and data types",
            "Apply basic data governance practices",
            "Understand when different storage types are useful",
        ),
    ),
    _immutable_record(
        number=5,
        title="Data Integration",
        skills=(
            "Build ETL and ELT workflows",
            "Ingest and transform batch data",
            "Improve data quality and traceability",
            "Create repeatable pipelines",
        ),
    ),
    _immutable_record(
        number=6,
        title="Data Warehousing",
        skills=(
            "Understand the warehouse lifecycle",
            "Use fact and dimension thinking",
            "Prepare data for reporting",
            "Apply basic dimensional modeling",
        ),
    ),
    _immutable_record(
        number=7,
        title="Data Platform Development",
        skills=(
            "Use Docker containerization",
            "Build APIs with FastAPI",
            "Work with Supabase and PostgreSQL",
            "Support platform setup and management",
        ),
    ),
    _immutable_record(
        number=8,
        title="Exploratory Data Analysis",
        skills=(
            "Explore trends and patterns in data",
            "Turn data into useful insights",
            "Create clear reports",
            "Build interactive dashboards",
        ),
    ),
    _immutable_record(
        number=9,
        title="Data Visualization",
        skills=(
            "Build dashboards in Power BI",
            "Use star schema for reporting",
            "Collaborate with UX designers on layout and usability",
            "Create Streamlit apps for interactive data experiences",
        ),
    ),
    _immutable_record(
        number=10,
        title="Big Data & Cloud Foundations",
        skills=(
            "Learn Databricks for large-scale data work",
            "Use PySpark for distributed data processing",
            "Build cloud knowledge with Azure",
            "Understand modern big data platforms",
        ),
    ),
    _immutable_record(
        number=11,
        title="Engineering Practices",
        skills=(
            "Use Git for version control",
            "Write clear technical documentation",
            "Turn business needs into working solutions",
            "Focus on maintainable and scalable work",
        ),
    ),
)


TECH_STACK_LAYERS = (
    _immutable_record(
        level=7,
        title="Delivery",
        technologies=("Streamlit", "Power BI", "FastAPI", "Databricks Dashboards"),
    ),
    _immutable_record(
        level=6,
        title="Orchestration & Reliability",
        technologies=("Airflow", "Docker", "Terraform", "pytest", "GitHub Actions"),
    ),
    _immutable_record(
        level=5,
        title="Processing & Transformation",
        technologies=("Pandas", "Spark/PySpark", "Databricks", "dbt Core", "Medallion Architecture"),
    ),
    _immutable_record(
        level=4,
        title="Ingestion & Integration",
        technologies=("ETL/ELT", "REST APIs", "Kafka", "Azure Data Factory"),
    ),
    _immutable_record(
        level=3,
        title="Platform & Storage",
        technologies=("S3", "PostgreSQL", "TimescaleDB", "DuckDB", "Snowflake", "Delta Lake"),
    ),
    _immutable_record(
        level=2,
        title="Data Modeling",
        technologies=("RDBMS", "3NF", "Dimensional Modeling", "Star Schema"),
    ),
    _immutable_record(
        level=1,
        title="Core Foundations",
        technologies=("Python", "SQL", "OOP", "Git/GitHub", "Bash"),
    ),
)

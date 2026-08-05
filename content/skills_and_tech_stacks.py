"""Data-driven Skills & Tech Stacks page content."""

from types import MappingProxyType


def _immutable_record(**values: object) -> MappingProxyType:
    return MappingProxyType(values)


COMPETENCY_STAGES = (
    _immutable_record(
        number=1,
        title="Core Foundations",
        skills=(
            "Build maintainable Python applications",
            "Apply object-oriented programming principles",
            "Query and manipulate data with SQL",
            "Work with virtual environments and dependencies",
            "Use version control and automated testing",
        ),
    ),
    _immutable_record(
        number=2,
        title="Data Modelling",
        skills=(
            "Design conceptual, logical, and physical data models",
            "Apply normalization and 3NF principles",
            "Work with primary and foreign key relationships",
            "Understand OLTP vs OLAP modelling requirements",
            "Apply dimensional modelling and star-schema concepts",
        ),
    ),
    _immutable_record(
        number=3,
        title="Platform & Storage",
        skills=(
            "Design databases, schemas, tables, and data types",
            "Choose appropriate transactional and analytical storage",
            "Work with relational, object, warehouse, and lakehouse storage",
            "Understand data lake and cloud-storage foundations",
            "Apply basic data governance and storage design principles",
        ),
    ),
    _immutable_record(
        number=4,
        title="Ingestion & Integration",
        skills=(
            "Design ETL and ELT workflows",
            "Integrate REST APIs and external data sources",
            "Work with batch and streaming ingestion patterns",
            "Validate incoming data and improve traceability",
            "Build repeatable and reliable ingestion pipelines",
        ),
    ),
    _immutable_record(
        number=5,
        title="Processing & Transformation",
        skills=(
            "Clean, transform, and enrich raw data",
            "Perform exploratory data analysis",
            "Build reusable transformation layers",
            "Process distributed and large-scale datasets",
            "Apply Medallion Architecture patterns",
        ),
    ),
    _immutable_record(
        number=6,
        title="Data Warehousing & Analytics Engineering",
        skills=(
            "Understand the data warehouse lifecycle",
            "Design fact and dimension tables",
            "Apply dimensional and star-schema modelling",
            "Build analytics-ready transformation layers",
            "Organize data marts for reporting and analysis",
        ),
    ),
    _immutable_record(
        number=7,
        title="Orchestration, Cloud & Reliability",
        skills=(
            "Orchestrate multi-step data workflows",
            "Containerize applications and data services",
            "Apply infrastructure-as-code principles",
            "Implement automated tests and CI/CD workflows",
            "Design observable and maintainable data pipelines",
        ),
    ),
    _immutable_record(
        number=8,
        title="Analytics & Delivery",
        skills=(
            "Prepare trusted datasets for reporting",
            "Turn analytical data into business insights",
            "Design dashboards and interactive reports",
            "Build data applications and API-based delivery layers",
            "Present data clearly for technical and non-technical users",
        ),
    ),
    _immutable_record(
        number=9,
        title="AI Engineering & AI Workflows",
        skills=(
            "Use AI coding assistants for development and debugging",
            "Use AI for codebase analysis, refactoring, and documentation",
            "Integrate ChatGPT/Codex, GitHub Copilot, and Claude into daily software and data engineering workflows",
        ),
        upcoming_title="Upcoming coursework",
        upcoming=(
            "Retrieval-Augmented Generation (RAG)",
            "Vector databases and embeddings",
            "LLMOps and AI application monitoring",
            "Tracing, evaluation, and governance",
            "Prompt engineering and AI-system reliability",
        ),
    ),
    _immutable_record(
        number=10,
        title="Agile Delivery & Collaboration",
        skills=(
            "Work with Agile and iterative delivery practices",
            "Plan work through backlogs, issues, and project boards",
            "Use branches, pull requests, and collaborative Git workflows",
            "Participate in code review and technical documentation",
            "Organize engineering work using Scrum/Kanban-style practices",
        ),
    ),
)

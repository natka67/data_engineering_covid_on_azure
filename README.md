### Sources
- **Public COVID-19 Data**:  
  - Data is sourced from publicly available COVID-19 datasets or API endpoints. These may include data feeds provided by public health organizations or governmental repositories.
- **Raw Data Files**:  
  - Data files (CSV, JSON, etc.) that contain COVID-19 statistics and related information. These files serve as the input for the ingestion pipeline.

---

### Resources on Azure
- **Azure Data Factory**: Central to this project, Azure Data Factory handles the orchestration of data movement. It utilizes pipelines, dataflows, and linked services to connect to external data sources, perform data ingestion, and trigger transformations.
- **Azure Storage Accounts**: For storing raw and processed data.  
- **Azure SQL Database/Cosmos DB**: Potential destinations for processed data, enabling further analysis and reporting.  
- **Resource Deployment Files**: Configuration files (like `publish_config.json`) are used to deploy and set up resources on the Azure environment.

---

### Transformations
- **Data Ingestion**:  Raw data is ingested from various sources into Azure via Data Factory pipelines.
- **Data Cleansing and Aggregation**: Using Azure Data Factory’s dataflows, the raw COVID-19 data is cleaned, aggregated, and standardized to prepare it for analysis.
- **Custom Serverless Processing**: Azure Functions (as seen with `function_app.py`) provide the capability to execute customized data transformations or orchestrate tasks that go beyond standard Data Factory operations.

---

### Project Goal
- **Build a Scalable Data Pipeline for COVID-19 Data**: The ultimate aim is to demonstrate how to construct an end-to-end data engineering solution on Azure. This solution handles:
- **Ingestion and Preparation**: Bringing raw COVID-19 data into a centralized system.
- **Transformation and Cleansing**: Applying necessary business logic to clean and prepare data.
- **Orchestration and Automation**: Leveraging Azure Data Factory to manage, automate, and monitor the data pipeline.
- **Facilitating Analysis**: Setting the stage for downstream analytical tasks and insights to inform decision-making.

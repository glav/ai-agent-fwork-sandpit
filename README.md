# AI Agent Framework Sandpit
A simple playpen to allow experimentation with the new AI Agent Framework

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Azure CLI
- Access to Azure OpenAI or Azure AI Foundry

## Getting Started

### 1. Azure CLI Authentication

This project uses Azure CLI credentials for authentication. You **must** authenticate with Azure before running the application:

```bash
az login
```

This command will open a browser window for you to sign in with your Azure credentials. The application uses `AzureCliCredential` which relies on this authentication.

### 2. Environment Variables Setup

The project requires environment variables to be configured in a `.env` file.

1. Copy the sample environment file:
   ```bash
   cp .env-sample .env
   ```

2. Edit the `.env` file and configure the following required variables:

   **For Azure OpenAI:**
   - `AZURE_OPENAI_API_KEY` - Your Azure OpenAI API key
   - `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI endpoint (e.g., `https://{your-resource}.openai.azure.com`)
   - `OPENAI_API_VERSION` - API version (default: `2024-02-15-preview`)

   **For Azure AI Foundry:**
   - `AZURE_AI_FOUNDRY_CONNECTION_STRING` - Your AI Foundry project connection string

   **Optional Configuration:**
   - `ENABLE_TRACE_LOGGING` - Set to `"true"` to enable detailed logging
   - `APPLICATION_INSIGHTS_CONNECTION_STRING` - For Application Insights integration
   - `OTEL_EXPORTER_OTLP_ENDPOINT` - OpenTelemetry collector endpoint
   - `ENVIRONMENT` - Environment name (e.g., `development`, `production`)
   - `DEBUG` - Set to `True` for debug mode

3. See `.env-sample` for a complete list of available configuration options and examples.

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python src/main.py
```

## Troubleshooting

- **Authentication errors**: Make sure you have run `az login` and successfully authenticated with Azure
- **Missing environment variables**: Verify your `.env` file is properly configured with all required variables
- **Connection errors**: Check that your Azure OpenAI/AI Foundry endpoints and credentials are correct

# AI Agent Framework Sandpit
A simple playpen to allow experimentation with the new AI Agent Framework

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) - Python package and project manager
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

   **For Azure AI Foundry:**
   - `AZURE_AI_PROJECT_ENDPOINT` - Your AI Foundry project connection string. eg. `https://{foundry-host}.services.ai.azure.com/api/projects/{foundry-project}`
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Your model deployment name eg. `gpt-4o`


3. See `.env-sample` for a complete list of available configuration options and examples.

### 3. Install Dependencies

This project uses `uv` for Python dependency management. Install dependencies with:

```bash
uv sync
```

### 4. Run the Application

Run the application using `uv`:

```bash
uv run src/basic_samples/main.py
```

## Troubleshooting

- **Authentication errors**: Make sure you have run `az login` and successfully authenticated with Azure
- **Missing environment variables**: Verify your `.env` file is properly configured with all required variables
- **Connection errors**: Check that your Azure OpenAI/AI Foundry endpoints and credentials are correct

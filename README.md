# magentic-one-edi-prototype

## Magentic One EDI Prototype
This is a simple prototyp using AutoGen Magentic One to resolve tasks related to EDI (Electronic Data Interchange).

## How to run
To use the AutoGen Magentic One Agents on OpenAI GPT-4o you need to have an OpenAI account and API key and need to set it in the file [./docker-compose-yml](./docker-compose.yml).

This prototype needs docker and docker-compose to run. To start the system, run the following command in the root directory of the project:

```bash
docker compose up
```

This will start 2 containers:

1. The AutoGen Magentic One Agent App - This app runs specific EDI related tasks using Magentic One and stores results in log files. After successful completion of the tasks the log files are being transformed in a structured JSON format.
2. The log file viewer API - This API runs a Flask web server and provides an endpoint to view the log files in a structured JSON format.

After the system is started you can launch the the [./visualize-logs.html](./visualize-log.html) UI to call the log file viewer API and display the log files in a user friendly way.
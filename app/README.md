# Autogent Magentic One App
The AutoGen Magentic One App is a simple prototype to resolve tasks related to EDI (Electronic Data Interchange) using AutoGen Magentic One. The app runs specific EDI related tasks using Magentic One and stores results in log files. After successful completion of the tasks the log files are being transformed in a structured JSON format.

The workflow execution is controlled by the [./run.sh](./run.sh) script. The script
1. Runs the specific EDI task and creates standard Python log files
2. Transforms the log files in a structured JSON format
- [ ] TODO: finaliz transformation
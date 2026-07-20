
## Deep Research

Deep Research is a Gradio-powered research assistant that uses AI agents to plan searches, gather information, write a detailed report, and send the result by email.

## What it does

- Accepts a research query from the user
- Plans a set of web searches for the topic
- Performs each search using an AI-powered search agent
- Writes a long-form markdown report from the gathered findings
- Sends the completed report as an email

## Setup

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key and any optional settings:

```env
OPENAI_API_KEY=your_api_key_here
DEFAULT_MODEL_NAME=gpt-5.4-mini
USE_EMAIL=true
HOW_MANY_SEARCHES=5
```
4. Run the program!
``` 
uv run app.py
```

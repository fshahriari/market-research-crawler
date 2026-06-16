# Market Research Crawler 🕵️‍♂️

A lightweight Python-based web crawler designed for automated market research. It searches the web for your specific topics and scrapes data to provide useful insights.

## Features
- **Dynamic Search:** Uses DuckDuckGo to perform searches without API restrictions.
- **Data Extraction:** Automatically scrapes titles and summaries from search results.
- **Clean Output:** Saves all gathered data into a structured `results.json` file.
- **Easy to Use:** Supports both direct URLs and search queries.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `duckduckgo-search`

## Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/fshahriari/market-research-crawler.git](https://github.com/fshahriari/market-research-crawler.git)
Navigate to the folder:

Bash
cd market-research-crawler
Create and activate a virtual environment:

Bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Usage
Run the script from your terminal:

Bash
python main.py
Enter a URL (e.g., https://www.python.org) or a Search Topic (e.g., iPhone 18).

Check the generated results.json file for the findings.

License
This project is open-source and available for learning purposes.

Built with ❤️ using Python.
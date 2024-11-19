## Recursive Web Crawler

This project is a recursive web crawler designed to extract webpage content and follow links up to a specified depth and page limit. The crawler supports flexible output options, including saving the results to a local JSON file or a MongoDB collection.

Features

Recursive Crawling: Crawl web pages recursively, up to a specified depth or page limit.
Content Extraction: Extract page text and hyperlinks from web pages.
Configurable Output: Save crawl results to a JSON file or a MongoDB database.
Robust Logging: Structured logging with error handling for debugging.

Project Structure

.
├── main.py                  # Entry point for the crawler
├── endpoint.py              # Core logic for recursive crawling
├── lib/
│   ├── extract.py           # Functions to fetch and parse webpage content
│   └── output.py            # Functions to save results to file or MongoDB



Requirements
Python 3.10+
Required libraries:
requests
beautifulsoup4
pymongo
structlog

Usage
Command-Line Interface
Run the crawler using main.py with the following arguments:

```bash
python main.py --url <URL> [--max-depth <DEPTH>] [--max-pages <PAGES>] --output-type <TYPE> [--output-path <PATH>] [--mongo-uri <URI>]
```

Arguments:
--url: The starting URL for the crawl (required).
--max-depth: Maximum recursive depth (default: 3).
--max-pages: Maximum number of pages to crawl (default: 10).
--output-type: Output type, either file or mongo (required).
file: Saves the results to a JSON file.
mongo: Saves the results to a MongoDB database.
--output-path: File path for saving JSON results (required if --output-type file).
--mongo-uri: MongoDB connection URI (required if --output-type mongo).


How It Works
Initialization:

The crawler is initialized with the specified URL, depth, and page limits.
Logging is configured using structlog.

Crawling:

The crawler fetches the webpage content using requests and parses it with BeautifulSoup.
Links matching the specified pattern are identified and recursively crawled.

Output:

Results can be saved to a local file (JSON format) or to a MongoDB collection using pymongo.

Code Details

main.py
Handles:
Argument parsing.
Logger setup.
Coordination between crawling (endpoint.recursive_crawl) and output handling.
endpoint.py

Core function:
recursive_crawl: Implements the recursive crawling logic, including link extraction, visited URL tracking, and recursion depth control.
lib/extract.py

Key function:
fetch_page_content: Fetches webpage content, extracts text, and identifies hyperlinks.
lib/output.py

Functions:
save_to_file: Saves the results as a JSON file.
save_to_mongo: Inserts the results into a MongoDB collection.


How to use:

Setup virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

```bash
python main.py --url <https://cloud.google.com/blog/topics/threat-intelligence> --max-depth <max number of recursions> --max-pages <number of pages> --output-type file --output-path <path to save file.json>
```

Save results to MongoDB:

```bash
python main.py --url <https://cloud.google.com/blog/topics/threat-intelligence> --max-depth <max number of recursions> --max-pages <max number of pages> --output-type mongo --mongo-uri <your mongo uri>
```


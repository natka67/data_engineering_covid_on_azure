import azure.functions as func
import logging
import json
import re
from bs4 import BeautifulSoup
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="parse_links", methods=["POST"])
def parse_links(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function "parse_links" started processing a request.')
    try:
        # Use requests.get() to retrieve the HTML content
        response = requests.get('https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page')
        # Get the raw HTML content from the response
        html_content = response.text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Prepare a list to hold the resulting link details
        results = []
        
        # Regex pattern to capture a year and month in the format "YYYY-MM"
        pattern = re.compile(r"(20\d{2})-(\d{2})")
        
        # Iterate over all <a> tags that have an href attribute
        for a in soup.find_all('a'):
            url = a.get('href')
            if url:
                # Search for the year-month pattern in the URL
                match = pattern.search(url)
                if match:
                    year, month = match.group(1), match.group(2)
                    # Only process links with a year 2024 or later
                    if int(year) >= 2024:
                        sink_folder = f"{year}/{month}"
                        # Derive the filename from the URL (everything after the last slash)
                        filename = url.split('/')[-1].strip()
                        results.append({
                            "url": url.strip(),
                            "sink_folder": sink_folder,
                            "filename": filename
                        })

        # Return the JSON array of results
        return func.HttpResponse(
            json.dumps(results),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Error processing HTML: {e}")
        return func.HttpResponse(
            f"Error processing the request: {str(e)}",
            status_code=500
        )

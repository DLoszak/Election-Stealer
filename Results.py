import requests
import logging
from bs4 import BeautifulSoup
from utils import results_url

# Function to fetch poll results with error handling and logging
def fetch_poll_results():
    try:
        response = requests.get(results_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = []
            answer_groups = soup.find_all("li", class_="pds-feedback-group")
            for group in answer_groups:
                try:
                    name = group.find("span", class_="pds-answer-text").text.strip()
                    percentage = group.find("span", class_="pds-feedback-per").text.strip()
                    results.append(f"{name}: {percentage}")
                except AttributeError:
                    logging.warning("Failed to parse poll result group.")
                    continue
            logging.info("Poll results successfully fetched and parsed.")
            return results
        else:
            logging.error(f"Failed to fetch poll results. Status Code: {response.status_code}")
            return ["Failed to retrieve results."]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching poll results: {e}")
        return [f"Error fetching poll results: {e}"]

# Function to display poll results with logging
def display_results():
    results = fetch_poll_results()
    for result in results:
        print(result)
        logging.info(f"Poll Result: {result}")

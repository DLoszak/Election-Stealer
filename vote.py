import requests
import logging
from bs4 import BeautifulSoup
from utils import vote_url, results_url, poll_data

# Headers copied from the browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Referer": "https://www.usatodaynetworkservice.com/tangstatic/html/pnjm/sf-q1a2z330306dc3.min.html",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
}

# Create a session to handle cookies
session = requests.Session()


def fetch_dynamic_data():
    """Fetch dynamic data such as the 'n' parameter required for the vote."""
    try:
        # Fetch the poll page to extract the 'n' parameter
        response = session.get(results_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # DEBUGGING: Print out the entire page content to inspect it
            logging.info(f"Poll page content:\n{soup.prettify()}")

            # Try finding the 'n' parameter in the script tag
            script_tag = soup.find('script', text=lambda t: t and 'n=' in t)
            if script_tag:
                n_value = script_tag.text.split('n=')[1].split('&')[0]
                logging.info(f"Fetched dynamic 'n' value: {n_value}")
                return n_value
            else:
                logging.error("Failed to find 'n' value on the page.")
                return None
        else:
            logging.error(f"Failed to load the poll page. Status Code: {response.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"Error while fetching dynamic data: {e}")
        return None


def submit_vote(instance_id):
    """Submit a vote using the dynamically fetched 'n' parameter."""
    try:
        # Fetch dynamic 'n' parameter
        n_value = fetch_dynamic_data()

        if not n_value:
            logging.error(f"Instance {instance_id}: Failed to retrieve dynamic parameters.")
            return

        # Update poll_data with the dynamically retrieved 'n' value
        poll_data['n'] = n_value

        # Use the session to make the request
        response = session.post(vote_url, data=poll_data, headers=headers)

        # Print detailed response information for debugging
        print(f"Response for instance {instance_id}:")
        print(f"Status Code: {response.status_code}")

        # Try to decode as UTF-8 for display
        try:
            decoded_response = response.content.decode('utf-8')
        except UnicodeDecodeError:
            decoded_response = response.content.decode('latin-1')

        print(f"Decoded Response Text: {decoded_response}")

        if response.status_code == 200:
            # Check if the response is not empty
            if decoded_response.strip():
                try:
                    response_json = response.json()  # Try parsing the response as JSON

                    # Check for the 'registered' keyword in the JSON response
                    if response_json.get("result") == "registered":
                        logging.info(f"Vote for Ethan Brezden submitted successfully from instance {instance_id}.")
                        print(f"Vote for Ethan Brezden submitted successfully from instance {instance_id}!")
                    else:
                        logging.warning(
                            f"Vote submission might have failed. Unexpected response content from instance {instance_id}.")
                        print(
                            f"Vote submission might have failed. Check the response content for instance {instance_id}.")
                except ValueError:
                    # If the response is not valid JSON, print it for debugging
                    logging.error(f"Unexpected non-JSON response for instance {instance_id}: {decoded_response}")
                    print(f"Unexpected non-JSON response for instance {instance_id}: {decoded_response}")
            else:
                logging.error(f"Empty response from server for instance {instance_id}")
                print(f"Empty response from server for instance {instance_id}")
        else:
            logging.error(f"Failed to submit vote from instance {instance_id}. Status Code: {response.status_code}")
            print(f"Failed to submit vote from instance {instance_id}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error submitting vote from instance {instance_id}: {e}")
        print(f"Error submitting vote from instance {instance_id}: {e}")


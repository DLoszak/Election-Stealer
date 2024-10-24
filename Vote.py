import requests
import logging
from utils import vote_url, poll_data


# Function to submit a vote with detailed success checks
def submit_vote(instance_id):
    try:
        response = requests.post(vote_url, data=poll_data)

        if response.status_code == 200:
            response_text = response.text.lower()

            if "thank you" in response_text or "vote has been recorded" in response_text:
                logging.info(f"Vote for Ethan Brezden submitted successfully from instance {instance_id}.")
                print(f"Vote for Ethan Brezden submitted successfully from instance {instance_id}!")
            else:
                logging.warning(
                    f"Vote submission might have failed. Unexpected response content from instance {instance_id}.")
                print(f"Vote submission might have failed. Check the response content. Instance {instance_id}")
        else:
            logging.error(f"Failed to submit vote from instance {instance_id}. Status Code: {response.status_code}")
            print(f"Failed to submit vote from instance {instance_id}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error submitting vote from instance {instance_id}: {e}")
        print(f"Error submitting vote from instance {instance_id}: {e}")

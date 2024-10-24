import logging

# Configure logging
logging.basicConfig(
    filename='voting_log.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Constants for poll URL and data
vote_url = "https://poll.fm/vote"
results_url = "https://poll.fm/14534440/results"

poll_data = {
    'p': '14534440',  # Poll ID
    'a': '64612987',  # Ethan Brezden's ID
    'b': '1',  # Button value
    'cookie': '1',  # Enable cookies
    'va': '16',  # Poll version
    'o': ''  # Other option left empty
}

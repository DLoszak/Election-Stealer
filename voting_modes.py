from concurrent.futures import ThreadPoolExecutor
import logging
import random
import time
from vote import submit_vote
from results import display_results
import threading

vote_tracker_lock = threading.Lock()

# Function for timed voting with logging and error handling
def voting_instance_timed(instance_id, min_time, max_time):
    vote_count = 0
    while True:
        submit_vote(instance_id)
        vote_count += 1
        logging.info(f"Instance {instance_id} has submitted {vote_count} votes.")
        print(f"Total votes submitted by instance {instance_id}: {vote_count}")

        display_results()

        try:
            wait_time = random.randint(min_time, max_time)
            logging.info(f"Instance {instance_id} waiting for {wait_time} seconds.")
            print(f"Instance {instance_id} waiting for {wait_time} seconds until the next vote...\n")
            time.sleep(wait_time)
        except Exception as e:
            logging.error(f"Error during waiting period in instance {instance_id}: {e}")
            print(f"Error during waiting period in instance {instance_id}: {e}")

# Function for goal-oriented voting with error handling and logging
def voting_instance_goal(instance_id, vote_goal, vote_tracker):
    while True:
        with vote_tracker_lock:
            if vote_tracker[0] >= vote_goal:
                logging.info(f"Instance {instance_id} stopping as goal of {vote_goal} votes has been reached.")
                break
        submit_vote(instance_id)
        with vote_tracker_lock:
            vote_tracker[0] += 1
            logging.info(f"Total votes submitted across all instances: {vote_tracker[0]}")
            print(f"Total votes submitted overall: {vote_tracker[0]}")

        display_results()

# Run multiple parallel voting instances with timed voting
def run_parallel_voting_timed(instances, min_time, max_time):
    try:
        with ThreadPoolExecutor(max_workers=instances) as executor:
            for i in range(instances):
                executor.submit(voting_instance_timed, i + 1, min_time, max_time)
        logging.info(f"Started {instances} parallel voting instances with timed delays.")
    except Exception as e:
        logging.error(f"Error starting parallel voting instances with timed voting: {e}")
        print(f"Error starting parallel voting instances with timed voting: {e}")

# Run multiple parallel voting instances with a goal in mind
def run_parallel_voting_goal(instances, vote_goal):
    vote_tracker = [0]  # Shared counter for total votes
    global vote_tracker_lock
    vote_tracker_lock = threading.Lock()  # Lock to ensure thread-safe updates
    try:
        with ThreadPoolExecutor(max_workers=instances) as executor:
            for i in range(instances):
                executor.submit(voting_instance_goal, i + 1, vote_goal, vote_tracker)
        logging.info(f"Started {instances} parallel voting instances working towards goal of {vote_goal} votes.")
    except Exception as e:
        logging.error(f"Error starting parallel voting instances with goal-oriented voting: {e}")
        print(f"Error starting parallel voting instances with goal-oriented voting: {e}")

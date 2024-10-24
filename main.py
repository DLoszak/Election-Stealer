from voting_modes import run_parallel_voting_timed, run_parallel_voting_goal
import logging

def main():
    try:
        # Get user inputs
        num_instances = int(input("Enter the number of parallel processes (threads): "))
        min_time = int(input("Enter the minimum time between votes (in seconds, 0 for goal-oriented mode): "))
        max_time = int(input("Enter the maximum time between votes (in seconds, 0 for goal-oriented mode): "))

        if min_time == 0 and max_time == 0:
            # Goal-oriented mode
            vote_goal = int(input("Enter the total number of votes to submit: "))
            run_parallel_voting_goal(num_instances, vote_goal)
        else:
            # Timed voting mode
            if min_time > max_time:
                logging.error("Minimum time cannot be greater than maximum time.")
                print("Error: Minimum time cannot be greater than maximum time.")
            else:
                run_parallel_voting_timed(num_instances, min_time, max_time)
    except ValueError as e:
        logging.error(f"Invalid input received: {e}")
        print(f"Invalid input: {e}")
    except Exception as e:
        logging.critical(f"Critical error in main execution: {e}")
        print(f"Critical error: {e}")

if __name__ == "__main__":
    main()

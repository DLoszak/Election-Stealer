Autovote Script
===============

Overview
--------

The **Autovote Script** is a Python program designed to automate the process of voting on a specific poll hosted on **Poll.fm**. It allows users to submit votes in a loop, either with a randomized delay between each vote or in a goal-oriented manner, where a target number of votes is submitted as quickly as possible. Additionally, it supports parallelism, meaning multiple threads can run concurrently to submit votes simultaneously, significantly increasing the rate of submission.

This script features:

*   Timed voting mode: Votes are submitted after a random delay between a minimum and maximum time set by the user.
    
*   Goal-oriented voting mode: The user sets a target number of total votes, and multiple threads work together to achieve this goal as fast as possible.
    
*   Extensive logging and error handling, allowing users to track voting progress and troubleshoot potential issues.
    

Features
--------

1.  **Randomized Timed Voting**: Set minimum and maximum wait times between votes. Each vote is submitted with a random delay within this range.
    
2.  **Goal-Oriented Voting**: Set a total number of votes to submit. The script will distribute the voting workload across multiple threads, which work together toward this goal.
    
3.  **Parallel Execution**: Run multiple instances (threads) to submit votes concurrently, speeding up the process.
    
4.  **Error Handling**: Includes robust error handling for network issues and invalid inputs.
    
5.  **Logging**: Logs detailed information about vote submissions, poll results, and any errors encountered during execution.
    

Requirements
------------

Before using this script, ensure you have Python 3.6 or higher installed, as well as the required libraries. You can install the required dependencies via pip (instructions below).

### Dependencies

*   **requests**: For making HTTP POST and GET requests.
    
*   **beautifulsoup4**: For parsing and extracting data from HTML.
    
*   **lxml**: Optional but recommended for faster HTML parsing with BeautifulSoup.
    

To install the required dependencies, run the following command:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepip install requests beautifulsoup4 lxml   `

How It Works
------------

1.  **User Inputs**: When the script starts, the user is prompted to input the following:
    
    *   The number of parallel processes (threads) to run.
        
    *   The minimum and maximum time (in seconds) between each vote (for timed voting mode).
        
    *   Alternatively, if the user sets both min and max time to 0, the script will enter goal-oriented mode and ask for a target number of votes to submit.
        
2.  **Voting Process**:
    
    *   **Timed Voting Mode**: The script submits a vote and waits for a random interval between the user-defined min and max times before submitting the next vote.
        
    *   **Goal-Oriented Mode**: The script runs multiple parallel threads, all working toward submitting a predefined number of total votes as quickly as possible.
        
3.  **Logging**: All events, including successful vote submissions, errors, and poll result retrievals, are logged to voting\_log.log. This file contains time-stamped information on the voting process.
    
4.  **Error Handling**: If the script encounters a network error, an invalid response from the server, or any other issue, it logs the error and continues execution where possible. Critical errors cause the script to terminate with an appropriate error message.
    

Usage
-----

### 1\. Setting Up the Script

1.  **Clone or Download the Script**:
    
    *   Clone this repository or download the script to your local machine.
        
2.  bashCopy codepip install requests beautifulsoup4 lxml
    

### 2\. Running the Script

To run the script, open your terminal or command prompt, navigate to the directory where the script is located, and run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepython autovote.py   `

### 3\. User Input Prompts

Once the script is running, you'll be prompted to provide the following information:

#### **Number of Parallel Processes**:

*   This is the number of voting instances (threads) you want to run in parallel. For example, entering 4 will create 4 threads, each submitting votes independently and concurrently.
    

#### **Timed Voting Mode**:

*   **Minimum Time (in seconds)**: Enter the minimum time (in seconds) between vote submissions for each thread.
    
*   **Maximum Time (in seconds)**: Enter the maximum time (in seconds) between vote submissions. Each vote submission will randomly occur within this time range.
    

#### **Goal-Oriented Mode**:

*   If you enter 0 for both the minimum and maximum time, the script will switch to goal-oriented mode, and you will be prompted to enter a **target number of total votes**. The script will then divide the workload across the threads, with all threads contributing toward the total.
    

### 4\. Log Files

The script generates a log file, voting\_log.log, where all activities (successful votes, errors, poll results, etc.) are recorded. You can check this file to monitor the progress of the voting process or troubleshoot any issues.

### Example Usage

#### Example 1: Timed Voting Mode

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sqlCopy codeEnter the number of parallel processes (threads): 3  Enter the minimum time between votes (in seconds, 0 for goal-oriented mode): 30  Enter the maximum time between votes (in seconds, 0 for goal-oriented mode): 60   `

In this example, 3 parallel threads will submit votes, with each thread waiting for a random period between 30 and 60 seconds between submissions.

#### Example 2: Goal-Oriented Mode

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   mathematicaCopy codeEnter the number of parallel processes (threads): 5  Enter the minimum time between votes (in seconds, 0 for goal-oriented mode): 0  Enter the maximum time between votes (in seconds, 0 for goal-oriented mode): 0  Enter the total number of votes to submit: 500   `

In this example, the script will create 5 parallel threads, all working toward submitting a total of 500 votes as quickly as possible.

Logs and Error Handling
-----------------------

The script uses the logging module to log all important events and errors. Here's what is logged:

1.  **Vote Submissions**: Whether a vote was successfully submitted or not, including instance IDs and timestamps.
    
2.  **Errors**: Any network errors, request failures, or issues with parsing poll results.
    
3.  **Poll Results**: Each time the script fetches and displays poll results, the output is logged.
    

Log files are saved in voting\_log.log, located in the same directory as the script.

### Example Log Entry:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   yamlCopy code2024-10-23 10:15:32,123 - INFO - Vote for Ethan Brezden submitted successfully from instance 1.  2024-10-23 10:15:45,456 - WARNING - Vote submission might have failed. Unexpected response content from instance 2.  2024-10-23 10:16:01,789 - ERROR - Failed to submit vote from instance 3. Status Code: 500  2024-10-23 10:16:15,321 - INFO - Poll Result: Candidate A: 45%, Candidate B: 30%, Candidate C: 25%   `

Potential Issues and Troubleshooting
------------------------------------

### 1\. **Network Issues**:

*   If you encounter network-related errors (e.g., connection failures or timeout errors), the script will log the issue and attempt to recover.
    

### 2\. **Incorrect Poll Response**:

*   If the response from the server doesn't contain the expected confirmation message (e.g., "Thank you for voting"), the script will log a warning. Check the logs for details on unexpected responses.
    

### 3\. **Invalid Inputs**:

*   The script checks for valid inputs (e.g., ensuring the minimum time is less than or equal to the maximum time) and will log an error if the inputs are invalid.
    

Customization
-------------

You can easily customize the script for other polls or settings by adjusting the poll\_data dictionary, which contains the form fields required to submit a vote.

*   **Poll ID** ('p'): Update this value if you want to vote in a different poll.
    
*   **Candidate ID** ('a'): Change this value to vote for a different candidate.
    
*   **Other Options** ('o', 'b', 'va', etc.): Modify these fields if required by the poll structure.
    

Disclaimer
----------

This script is intended for educational purposes only. Please ensure you have permission to automate votes on any poll before using this script. Using automated scripts for voting may violate the terms of service of the poll provider or website.

Conclusion
----------

The Autovote Script is a versatile and efficient way to automate voting processes on Poll.fm. Whether you're looking to submit votes in timed intervals or reach a specific vote goal as fast as possible, this script provides the necessary functionality with extensive logging and error handling to ensure smooth execution.
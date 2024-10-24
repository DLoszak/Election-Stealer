Autovote Script - Modular Version
=================================

Overview
--------

The **Autovote Script** is a Python program designed to automate the process of voting on a specific poll hosted on **Poll.fm**. The script has been broken into modular components to make the code more manageable, easier to extend, and easier to debug. The script allows users to submit votes either with a randomized delay between each vote or in a goal-oriented manner, where a target number of votes is submitted as quickly as possible. Additionally, it supports parallelism, meaning multiple threads can run concurrently to submit votes simultaneously, increasing the voting rate.

Features
--------

1.  **Randomized Timed Voting**: Set minimum and maximum wait times between votes, with each vote being submitted after a random delay within this range.
    
2.  **Goal-Oriented Voting**: Set a total number of votes to submit. Multiple threads work together to achieve this target as quickly as possible.
    
3.  **Parallel Execution**: Run multiple instances (threads) concurrently to increase voting speed.
    
4.  **Logging**: Logs detailed information about vote submissions, poll results, and errors encountered during execution.
    
5.  **Error Handling**: Includes robust error handling for network issues, invalid inputs, and other potential problems.
    

Requirements
------------

Ensure you have Python 3.6 or higher installed before running this script.

### Dependencies

The required dependencies can be installed using the following command:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepip install requests beautifulsoup4 lxml   `

*   **requests**: For making HTTP POST and GET requests.
    
*   **beautifulsoup4**: For parsing and extracting data from HTML.
    
*   **lxml**: (Optional) Recommended for faster HTML parsing with BeautifulSoup.
    

Modular Breakdown
-----------------

The script has been split into the following Python files:

1.  **main.py**: The entry point for the script where user inputs are handled, and the appropriate voting mode (timed or goal-oriented) is selected.
    
2.  **vote.py**: Contains the logic for submitting a vote and ensuring the vote is processed correctly.
    
3.  **results.py**: Handles fetching and displaying the poll results.
    
4.  **voting\_modes.py**: Implements the logic for timed voting and goal-oriented voting using multiple threads.
    
5.  **utils.py**: Contains utility functions such as the logging setup and constants (e.g., URLs, form data).
    

### How It Works

1.  **User Inputs**:
    
    *   The user is prompted to provide the number of parallel processes (threads), the minimum and maximum wait times between votes (for timed voting), or a target number of votes (for goal-oriented voting).
        
2.  **Voting Process**:
    
    *   **Timed Voting Mode**: Votes are submitted at random intervals between the user-specified min and max times.
        
    *   **Goal-Oriented Mode**: Multiple threads work together to achieve the total number of votes as quickly as possible.
        
3.  **Logging**: All actions, including successful votes, poll results, and errors, are logged to voting\_log.log.
    
4.  **Error Handling**: Network errors, server responses, and other issues are logged, allowing the script to continue or stop depending on the severity of the error.
    

Usage
-----

### 1\. Setting Up the Script

1.  **Clone or Download** the repository.
    
2.  **Install the dependencies** using the following command:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepip install requests beautifulsoup4 lxml   `

### 2\. Running the Script

To start the script, navigate to the directory where the files are located and run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepython main.py   `

### 3\. User Input Prompts

You will be prompted to enter the following information:

*   **Number of Parallel Processes (threads)**: The number of voting instances to run concurrently.
    
*   **Timed Voting Mode**:
    
    *   **Minimum Time (in seconds)**: The minimum time between votes for each thread.
        
    *   **Maximum Time (in seconds)**: The maximum time between votes.
        
*   **Goal-Oriented Mode**:
    
    *   If you enter 0 for both the minimum and maximum times, you will be prompted to enter the **target number of total votes**. The script will distribute the workload across the threads to achieve this goal.
        

### 4\. Logs and Error Handling

The script generates a log file, voting\_log.log, which stores information about vote submissions, errors, and poll results. This file can be used to monitor the progress of the voting process or troubleshoot any issues.

#### Example Log Entry:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   yamlCopy code2024-10-23 10:15:32,123 - INFO - Vote for Ethan Brezden submitted successfully from instance 1.  2024-10-23 10:15:45,456 - WARNING - Vote submission might have failed. Unexpected response content from instance 2.  2024-10-23 10:16:01,789 - ERROR - Failed to submit vote from instance 3. Status Code: 500  2024-10-23 10:16:15,321 - INFO - Poll Result: Candidate A: 45%, Candidate B: 30%, Candidate C: 25%   `

Example Usage
-------------

### Timed Voting Mode

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sqlCopy codeEnter the number of parallel processes (threads): 3  Enter the minimum time between votes (in seconds, 0 for goal-oriented mode): 30  Enter the maximum time between votes (in seconds, 0 for goal-oriented mode): 60   `

In this example, 3 parallel threads will submit votes, with each thread waiting for a random period between 30 and 60 seconds between submissions.

### Goal-Oriented Mode

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   mathematicaCopy codeEnter the number of parallel processes (threads): 5  Enter the minimum time between votes (in seconds, 0 for goal-oriented mode): 0  Enter the maximum time between votes (in seconds, 0 for goal-oriented mode): 0  Enter the total number of votes to submit: 500   `

In this example, 5 parallel threads will work together to submit a total of 500 votes as quickly as possible.

Customization
-------------

You can easily customize the script for different polls by modifying the poll\_data dictionary in utils.py:

*   **Poll ID** ('p'): Change this value to the ID of the poll you want to vote on.
    
*   **Candidate ID** ('a'): Set this to the candidate you want to vote for.
    
*   **Additional Options** ('o', 'b', 'va', etc.): Modify these fields if needed to fit the poll's structure.
    

Potential Issues and Troubleshooting
------------------------------------

1.  **Network Issues**:
    
    *   If network errors occur, the script logs the issue and attempts to continue.
        
2.  **Incorrect Poll Response**:
    
    *   If the poll server doesn't return the expected confirmation message (e.g., "Thank you for voting"), the script logs a warning.
        
3.  **Invalid Inputs**:
    
    *   The script validates user inputs (e.g., ensuring the minimum time is less than the maximum) and logs errors if invalid data is entered.
        

Disclaimer
----------

This script is intended for educational purposes only. Please ensure you have permission to automate votes on any poll before using this script. Using automated scripts for voting may violate the terms of service of the poll provider or website.

Conclusion
----------

The modular **Autovote Script** provides a flexible and efficient way to automate voting on **Poll.fm**. With its robust error handling, parallel execution, and flexible voting modes, you can submit votes in timed intervals or target a specific vote count quickly. The modular design ensures the script is easy to extend, maintain, and customize for different use cases.
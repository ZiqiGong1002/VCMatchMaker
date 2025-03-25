Founder-Investor Compatibility Matcher (Jupyter Notebook Version)

##Overview
This Jupyter Notebook uses Google’s Gemini API to evaluate compatibility between startup founders and potential investors using natural language processing. It computes a score from 0 to 100 for each investor and ranks them based on how well they match a selected founder.


##Approach
The notebook follows these key steps:

Load founder and investor datasets (founders.csv, investors.csv)

Select a specific founder to match

Generate prompt messages and send them to the Gemini API

Handle API errors with retry logic

Output ranked match results as a CSV file


##Suggested Enhancements
Batch Matching: Support multiple founders at once for large-scale processing

Rate Limit Handling: Use adaptive delays to avoid hitting API rate limits

Dynamic Thresholds: Allow users to filter results based on minimum score thresholds

Secure API Key Management: Store keys in .env files or environment variables
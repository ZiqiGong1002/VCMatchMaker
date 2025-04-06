
## How It Works

1. **Data Collection**  
   - `founders.csv` contains structured data about startup founders.
   - `investor.json` includes investor information (manually curated or scraped).
   - `investor_json_to_csv.py` converts the JSON into a usable CSV format.

2. **Matching & Scoring**  
   - The notebook `assignment1_ranking.ipynb` uses an LLM to analyze the compatibility between each founder and investor.
   - Scoring considers various dimensions such as industry fit, stage preference, geographic alignment, and strategic value.
   - A ranked list of investors is generated for each founder.

3. **Sample Outputs**  
   - Outputs may include a CSV or markdown table showing top-N investor matches for each founder with scores and reasoning.

## Dependencies

To run the project, install the following:

```bash
pip install pandas openai jupyter

# Job Data Processor

This script fetches the job data I had inside an online Job Application Tracker and saves it in both JSON and Excel formats with timestamps. This entire thing was generated using Cursor AI Composer agents.

## Setup

1. Navigate to the job_tracker directory:

```bash
cd job_tracker
```

2. Create a virtual environment in the current directory:

```bash
# On Windows
python -m venv venv

# On macOS/Linux
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:

```bash
# Using the activated virtual environment's pip
pip install -r requirements.txt

# Or if the above doesn't work, you can explicitly use the virtual environment's Python:
# On Windows
.\venv\Scripts\python.exe -m pip install -r requirements.txt

# On macOS/Linux
./venv/bin/python -m pip install -r requirements.txt
```

5. Create a `.env` file in the current directory with the following content:

```
API_KEY=your_api_key_here
BEARER_TOKEN=your_bearer_token_here
API_ENDPOINT=your_api_endpoint_here
```

## Usage

1. Ensure you're in the job_tracker directory and the virtual environment is activated
2. Run the script using the virtual environment's Python:

```bash
# Using the activated virtual environment
python job_data_processor.py

# Or explicitly using the virtual environment's Python:
# On Windows
.\venv\Scripts\python.exe job_data_processor.py

# On macOS/Linux
./venv/bin/python job_data_processor.py
```

The script will:

- Fetch data from the configured API endpoint
- Save the data as JSON in `job_tracker/output/json/`
- Save the data as Excel in `job_tracker/output/excel/`
- Files are named with timestamps (format: `job_data_YYYYMMDD_HHMMSS.{json|xlsx}`)

## Output Structure

```
job_tracker/
├── .env
├── job_data_processor.py
├── requirements.txt
├── venv/
└── output/
    ├── json/
    │   └── job_data_YYYYMMDD_HHMMSS.json
    └── excel/
        └── job_data_YYYYMMDD_HHMMSS.xlsx
```

## Environment Variables

- `API_KEY`: Your API key for authentication
- `BEARER_TOKEN`: Bearer token for API authentication
- `API_ENDPOINT`: The URL of the API endpoint

## Troubleshooting

If you encounter package compatibility issues:

1. Delete the `venv` directory
2. Create a new virtual environment
3. Install the dependencies using the explicit path to the virtual environment's pip:

```bash
# On Windows
.\venv\Scripts\python.exe -m pip install -r requirements.txt

# On macOS/Linux
./venv/bin/python -m pip install -r requirements.txt
```

## Notes

- The `.env` file is not checked into version control for security
- Make sure to keep your API credentials secure
- The script creates necessary output directories automatically

# Google CSE Medical School Search 

This Python script uses the Google Programmable Search Engine (PSE) API to look up specific information related to a list of medical schools. It searches for the URL of each medical school and then looks up the count of "biomedical informatics" on that site.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The script has the following dependencies:

1. requests - for making HTTP requests.
2. urllib - for parsing URLs.
3. re - for regular expression operations.
4. time - for handling time-related tasks.

You need to install these dependencies using pip:

\```sh
pip install requests urllib3
\```

*Note: `re` and `time` are both part of Python's standard library and thus do not require separate installation.*

### Configuration

This script uses Google Programmable Search Engine API, so it requires an API Key and a Programmable Search Engine ID to run. You have to replace the placeholders with your actual API Key and Programmable Search Engine ID:

\```python
cse_id = "your-programmable-search-engine-id"
api_key = "your-api-key"
\```

To obtain your own Programmable Search Engine ID and API key:

1. Visit [Google Cloud Console](https://cloud.google.com/console).
2. Create a new project.
3. Enable Custom Search API for your project.
4. Go to Credentials, create an API key and copy it.
5. Visit [Programmable Search Engine](https://programmablesearchengine.google.com/about/) to create a new Programmable Search Engine and get the Engine ID.

### Running the Script

To run the script, simply use a Python interpreter:

\```sh
python your_script.py
\```

## Description of the script

The script consists of three main functions:

1. `google_search(search_term, api_key, cse_id, **kwargs)`: This function performs a search on the Google Programmable Search Engine with the given search term.

2. `get_school_url(school_name)`: This function gets the URL of a school by performing a Google search and returning the `netloc` of the first result.

3. `get_n_results(query)`: This function returns the total number of search results for a given query.

The script then creates a list of medical schools and iterates over this list. For each school, it attempts to retrieve the school's URL and the number of "biomedical informatics" results from the school's website. The results are then printed to the console.

## License

This project is licensed under the MIT License.

## Acknowledgments

* Google Programmable Search Engine API

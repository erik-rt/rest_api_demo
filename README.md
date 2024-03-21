# Flask REST API Demo

## Dataset

In order to query the endpoint, the data must first be loaded into the SQLite database. Download the dataset provided in the Google Doc, name it `openblocklabs-dataset.csv` and put it in the root directory.

## Running the App

This project uses the [Poetry](https://python-poetry.org/docs/) Python package management tool. You will need to install it to get set up. Once installed, clone the repo and step into the root directory. From there, run `poetry install` to install dependencies. You can then run `poetry shell` to activate the virtual environment for the project. Once ready, run `poetry run python main.py`. This will launch the Flask application which can be accessed at `http://127.0.0.1:5000`. This will lead you to the Swagger UI for the app.

### Authorization

The API uses a simple bearer token scheme. In this implementation, when the app starts it simply looks for an environment variable called `BEARER_TOKEN` and loads the value as the bearer token. When you make calls to the API, you will pass this token in your request. In order for this to work, you will have to rename the provided `.env.sample` file to `.env` and add the token there.

An example query to the API is `curl "http://127.0.0.1:5000/api/wallet?wallet_address=0x1155b614971f16758c92c4890ed338c9e3ede6b7&from_date=2024-01-29&to_date=2024-01-31" -H "Authorization: Bearer {token}"`

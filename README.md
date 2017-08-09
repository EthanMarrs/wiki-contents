# Wiki-Contents

A simple app for viewing Wikipedia contents pages.

## Getting Started

1. Download the application from `https://github.com/EthanMarrs/wiki-contents/archive/master.zip`

2. Unzip the archive:

            $ unzip wiki-contents-master.zip

3. Create a Python3 virtual environment (optional):

            $ python3 -m venv env

4. Activate the environment (optional):

            $ source env/bin/activate

5. Navigate into the `wiki-contents-master` directory:

            $ cd wiki-contents-master

6. Install the required packages for the application:

            $ pip install -e .

7. Run the application:

            $ pserve production.ini

8. Navigate to `http://localhost:6543/` in your browser

## Additionally

To run the tests (from the root directory):

            $ pip install -e ".[testing]"
            $ pytest

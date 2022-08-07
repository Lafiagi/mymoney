## Welcome to the GeekTrust Test
‘MyMoney’ is a platform that lets investors track their consolidated portfolio value across equity, debt, and gold.

## Installation and execution
 - Install python 3
 - Make current directory a virtual environment using `python3 -m venv .`
 - Run `pip3 install -r requirements.txt`
 - Run `pip3 install -r requirements.dev.txt`
 - Start app via command: `python3 geektrust.py <file_path>`
 - To run with test data:`python3 geektrust.py fixtures/fixture_rebalaceable.txt`
 - To run with test data(CANNOT_REBALANCE):`python3 geektrust.py fixtures/fixture_not_rebalaceable.txt `
 - Run test via command: `python3 -m unittest discover tests/`
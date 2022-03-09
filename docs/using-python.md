# Using Python on your own computer

To run one of the GLAM Workbench repositories within a dedicated Python environment on your own computer, you need to set up the necessary software. This approach requires familiarity with the command line and the ability to install and manage new software. You will, however, have full control over your working environment.

## Setting up your local environment

1. Create and activate a Python virtual environment (Python >= 3.8 should be ok). I use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to create and manage Python versions and environments.
2. On the command line, use `git clone` to create a local version of the GLAM Workbench repository, eg. `git clone https://github.com/GLAM-Workbench/trove-newspapers.git`
3. On the command line, use `cd` to move into the `notebooks` folder of the newly-cloned repository, eg. `cd trove-newspapers/notebooks`
4. On the command line, run `pip install -r requirements.txt` to install the required Python packages.

## Running Jupyter Lab

1. On the command line, run `jupyter lab` – to start Jupyter.
2. A browser window should open automatically. If not, copy and paste the url from the command line to your web browser.
3. To shut down your Jupyter Lab session hit ++ctrl+c++ on the command line.


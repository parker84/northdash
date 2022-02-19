north-dash
==============================

Status dashboard for Canada, a single place to quick understanding of how Canada is faring, based on the data.

### Table of Contents
- [Getting Started](#get-started)
- [Project Organization](#project-organization)

## [Getting Started](#get-started)

### Setup environment:
```sh
# for mac
virtualenv ./venv -p python3.9
source ./venv/bin/activate
pip install -r ./requirements
```

### Downloading the data

StatsCan:
1. [Physical flow account for greenhouse gas emissions, annual](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810009701)
2. [Low income statistics by age, sex and economic family type, annual](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013501)
3. [Gross domestic product (GDP) at basic prices, by industry, provinces and territories, annual (x 1,000,000)](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610040201)
4. [Consumer Price Index, monthly, not seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401)
5. [Labour force characteristics by province, monthly, seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028703)
6. [Gross domestic product (GDP) at basic prices, by industry, monthly (x 1,000,000)](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610043401)
7. [Employment and average weekly earnings (including overtime) for all employees by province and territory, monthly, seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410022301&pickMembers%5B0%5D=2.2&pickMembers%5B1%5D=3.1&cubeTimeFrame.startMonth=07&cubeTimeFrame.startYear=2021&cubeTimeFrame.endMonth=11&cubeTimeFrame.endYear=2021&referencePeriods=20210701%2C20211101)

### Preparing the Data
```sh
export PYTHONPATH="/Users/brydonparker/Documents/projects/side_projects/north-dash" # change to top of this repo 
python ./src/data/load_csvs_into_db.py

```

### Launch the dashboard locally:
```sh
export PYTHONPATH="/Users/brydonparker/Documents/projects/side_projects/north-dash" # change to top of this repo on your mac
strealit run ./src/visualization/dash.py
```

## [Project Organization](#project-organization)

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

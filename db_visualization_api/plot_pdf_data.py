# Importing the pdf database api:
from pdf_parsing_package import pdfdb_api

# Importing data visualization packages:
import plotly as plt
import dash

# Importing data management packages:
import pandas as pd

# Objects that connects to the pdf database and provides all plotting api:
class pdf_plot(object):
    """
    Main object contains all the methods that plot data extracted from the pdf
    parser database via the pdf parsing data api.

    Parameters
    ----------
    pdfdb_api : pdf parsing package database object.
        This parameter is the python object that connects to the sqlite database
        containing pdf data. A pdfdb_api.pdf_db() object intialized with a path string
        to the database is input into the pdf_plot method as its data query api
        will be used to provide the data being plotted.
    """
    def __init__(self, pdfdb_api):

        # Declaring the database api object as an instance variable:
        self.db_api = pdfdb_api

        # TODO: Once dunder method updated in the db_api, print debug statement.

# TODO: Write Methods described in yellow pages.


# Testing:
test = pdfdb_api.pdf_db('/home/matthew/Documents/test_pdf_databases/pdf_db')
plot_test = pdf_plot(test)

# Data analysis in Python using pandas

**Pandas** is an open source Python Library that provides high-performance data manipulation and analysis. With the combination of Python and pandas, you can accomplish five typical steps in the processing and analysis of data, regardless of the origin of data: load, prepare, manipulate, model, and analyze.

There are many options when working with the data using pandas. The following list shows some of the things that can be done using pandas.

* Cleaning data by removing or replacing missing values
* Converting data formats
* Sorting rows
* Deleting or adding rows and columns
* Merging or joining DataFrames
* Summarizing data by pivoting or reshaping
* Creating visualizations

This list is far from complete. See the pandas [documentation](https://pandas.pydata.org/docs/) for more of what you can do.

This workshop walks you though some of the most interesting features of pandas using structured data that contains information about the boroughs in London. You can download the data used in the tutorial from [data.gov.uk](https://data.gov.uk/dataset/248f5f04-23cf-4470-9216-0d0be9b877a8/london-borough-profiles-and-atlas).
 
## Getting Started with Jupyter Notebooks

Instead of writing code in a text file and then running the code with a Python command in the terminal, you can do all of your data analysis in one place. Code, output, tables, and charts can all be edited and viewed in one window in any web browser with [Jupyter Notebooks](https://jupyter.org/). As the name suggests, this is a notebook to keep all of your ideas and data explorations in one place. In this tutorial, you use [IBM Watson Studio](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/overview-ws.html) to run a notebook. For this, you need a free IBM Cloud account. The following steps show you how sign up and get started. When you have the notebook up and running, you can go through the notebook.

Jupyter notebooks are an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text.

In this workshop we will use IBM Watson Studio to run a notebook. For this you will need an IBM Cloud account. The following steps will show you how sign up and get started. When you have the notebook up and running we will go through the notebook.

If you have not already done so, make sure that you do the work for your [project setup](../project-setup/README.md)

## Load and Run a Notebook

* In your project, click `Add to project` and choose `Notebook`:

![Add notebook](../assets/images/setup/cpd-add-notebook.png)

* Choose New notebook `From URL`. Give your notebook a name and copy the URL `https://github.com/IBM/python-and-analytics/blob/master/notebooks/UK-workshop-pandas.ipynb`. Click `Create`:

![Notebook from URL](../assets/images/setup/cpd-notebook-from-url.png)

Spend some time looking through the sections of the notebook to get an overview. A notebook is composed of text (markdown or heading) cells and code cells. The markdown cells provide comments on what the code is designed to do.

You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook or hitting the keyboard short cut to run the cell (Shift + Enter but can vary based on platform). While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

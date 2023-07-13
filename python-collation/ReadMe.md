# How to install and launch Jupyter (for collationWorkspace)

## Requirements
- PyCharm

## Steps
If you do not have a `venv` folder -- or configured a PyCharm project -- in your `python-collation` directory; follow all of the steps from the beginning. Otherwise, you can skip to Step 3. 

1. Open PyCharm and check for any updates.Go to File,  Open, and with PyCharm's file explorer, open the `collationWorkspace\python-collation\` directory located in your repository. Open the folder as a project. 

2. A message should appear saying that the Python interpreter is missing/cannot be found. Click 'Configure a Python interpreter' then 'Add New Interpreter'. The Python Environment location should be located in `collationWorkspace\python-collation\`. If the location is correct, click on 'OK' and create the new Python environment. When the process is completed, you can move onto the next step.

3. Go to the Terminal and type in `pip install jupyter`. Let everything install until nothing is being processed.

4. Open up the Python terminal, and enter `jupyter notebook` to launch the Jupyter Notebook environment.

5. Your browser should automatically pop up and redirect you to the Jupyter Notebook environment. If not, put in localhost:8888/tree in your browser. Then you are all set :)


```python

```

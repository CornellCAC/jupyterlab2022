# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Jupyter Notebook Document

# ## *Literate analysis* in Jupyter Notebook
#
# In *literate analysis*, **documentation**, **specification**, **explanation**, **interpretation,** and **code** co-exist in a single document that presents the analysis process in a narrative format.
#
# In contrast to scripts, where code is the default kind of content and everything else must be shoe-horned into comments, notebooks are based on **cells**. 
#
# **Cells can be:**
#
# - *Markdown* formatted text cells
# - *Code* cells (python code is default in python notebooks but others are possible)
# - *Raw*, unformatted text
#

# ### Code Cells
#
# Code and results appear in specially designated content blocks.
# Execute a cell with <kbd>shift</kbd> + <kbd>return</kbd> or use the <kbd>&#9654;</kbd> button in the toolbar.

2 + 2 

# + [markdown] tags=[]
# ### Markdown Cells
# Markdown cells support a range of formatting options via [Markdown](https://daringfireball.net/projects/markdown/) and html5
#
# - *italics* 
# - **bold**
# - `code`
# - [links](https://jupyterlab.readthedocs.io/)
# - Inline LaTeX equations: $E = mc^{2}$
#
#
# \begin{equation}
# e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i
# \end{equation}
# -

# ### Raw Cells
#
# Raw cells show their contents. For example, the raw cell below shows the raw markdown from the cell above. 

# + active=""
# - *italics* 
# - **bold**
# - `code`
# - [links](https://jupyterlab.readthedocs.io/)
# - Inline LaTeX equations: $E = mc^{2}$
#
# \begin{equation}
# e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i
# \end{equation}
# -

# ## Hierarchical Organization
#
# Markdown supports six levels of headers to organize your document. Headers are text preceded by one to six hash symbols. The more hash symbols, the lower the level. 
#
# The outline pane on the left side shows the document outline and permits quick navigation. 
#

# + active=""
# ```
# # H1 heading (top level header)
# ## H2
# ### H3
# #### H4
# ##### H5
# ###### H6 (deepest level header)
# ```
# -





# +
# scroll down #
# -







# ### Heading Anchors

# [Code Cells](#Code-Cells)
#
# `[Code Cells](#Code-Cells)`

# ---

# + [markdown] tags=[]
# # Jupyter Interface
#
# ## Panels
#
# 1. File browser
# 2. Active kernel list
# 3. Outline view
# 4. Extensions
# 5. Inspector
# 6. Debug
#
# ## Menus
#
# - View > Activate Command Palette
# - Edit > Split / Merge Cells
#
# ## Documents
#
# 1. Notebooks
# 2. Consoles
# 3. Terminals (to underlying OS)
# -

# ## Editing Notebooks

# ### Re-order Cells
#

# + [markdown] tags=[]
# #### <span style="color:red"> Move me! </span>
# -

# ### Multiple Cursors

# Sometimes, you need to edit several places at once. Press command (macOS) or alt (Windows) and click to place additional cursors. 

# Change the 4 "dd"s to "gg"
+ dd.theme_bw()
+ dd.theme(figure_size=(10,6))
+ dd.theme(axis_text_x=dd.element_text(angle=30, hjust=1))


# ---

# # Features

# ## Execute Terminal Commands in host system

# ! ls

# + language="bash"
# #Unix hosts only
# ls
# -

# ### Jupytext Extension
#
# Pair the notebook with a "lightscript" file. Lightscript is can be executed like a python script file (.py) but also contains all the info needed to be reconstituted into a jupyter notebook. It strips out non-content metadata in the process, so lightscript files are a good choice to use with github (the file differences will only be actual differences in content). 
#
# With lightscript, you can also tag individual cells to be active/inactive only in certain formats. This is useful when you are writing a notebook that uses special notebook-only features that should also be runnable as a script.
#
# Use the *Pair Notebook with Lightscript* command in *View > Activate Command Palette*. 
#
# Refer to the Jupytext Manual [https://jupytext.readthedocs.io/en/latest/install.html](https://jupytext.readthedocs.io/en/latest/install.html) for more details.





# ### TQDM
#
# A popular progress bar tool integrated with many data science packages.

# + tags=["active-ipynb"]
# # has active-ipynb tag
# from tqdm.notebook import tqdm

# + tags=["active-py"]
# has active-py tag
from tqdm import tqdm

# +
import time

for i in tqdm(range(20)):
    time.sleep(.5)
# -

# ### Time and Timeit cell magics

# %%time
for i in tqdm(range(20)):
    time.sleep(.5)

# %%timeit
sum(x**2 for x in range(1,100000,10))

# ### Jupyter Widgets
#
# Widgets are a collection of simple interactive elements that can be used to create a GUI in Jupyter. 
#
# Uses:
#
# - enhance teaching and communication
# - support specialized interactive data analysis
# - create simple interfaces for human coding tasks like tagging, sorting, ranking or classifying.  
#
#
# https://ipywidgets.readthedocs.io/en/stable/lite/lab/

import ipywidgets as widgets
from IPython.display import display

date_w = widgets.DatetimePicker(
    description='Pick a Time',
    disabled=False
)
display(date_w)

print(date_w.value)



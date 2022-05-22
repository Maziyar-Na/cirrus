
# coding: utf-8

# # Publish
# ---
# This notebook publishes resources needed by Cirrus users. It is mainly intended for use by Cirrus developers.

# ## Setup
# ---

# In[ ]:


# To ease development, each time a cell is run, all modules will be reloaded.
#get_ipython().magic('load_ext autoreload')
#get_ipython().magic('autoreload 2')


# In[ ]:


import logging
import sys
import atexit


# In[ ]:


# Cirrus produces logs, but they will not show unless we add a handler that prints.
from cirrus import utilities
utilities.set_logging_handler()


# In[ ]:


from cirrus import automate
from cirrus import setup


# ## Lambda package
# ---
# When Cirrus users run the setup script, a serverless function (AWS Lambda function) is created. The Lambda package provides the code for it.

# In[ ]:


automate.make_lambda_package(setup.PUBLISHED_BUILD + "/lambda_package", setup.PUBLISHED_BUILD + "/executables")


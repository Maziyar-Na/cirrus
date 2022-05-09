
# coding: utf-8

# # Build
# ---
# This notebook builds Cirrus. It is mainly intended for use by Cirrus developers to push a new version of the software.

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
import subprocess


# In[ ]:


# Cirrus produces logs. Here we enable printing them in the notebook
from cirrus import utilities
utilities.set_logging_handler()


# In[ ]:


from cirrus import automate
from cirrus import setup


# ## Ubuntu (parameter server)
# ---
# Cirrus parameter server is optimized for Ubuntu. In this section we create an executable for the parameter server.

# ### Build image
# First, we create a "build image", which is an AMI on which we've set up the proper environment for building Cirrus. Making the build image is separated from making the executables because the build image will rarely need to be remade, whereas the executables will need to be remade for each new version of the system.

# In[ ]:


automate.make_ubuntu_build_image("cirrus_ubuntu_build_image")


# ### Executables
# Second, we compile the Cirrus parameter server (using the build image) and publish its executables.
# 
# The executables are published to the `cirrus-public` S3 bucket.

# In[ ]:


automate.make_executables(
    setup.PUBLISHED_BUILD + "/executables/ubuntu",
    ("self", "cirrus_ubuntu_build_image"),
    "ubuntu"
)


# ## Amazon Linux (Lambdas)
# ---
# AWS Lambdas run on an Amazon Linux image. Here we build the Cirrus binaries that runs on those AWS Lambdas.

# ### Build image
# Here we create an image used to compile the Cirrus workers executables.

# In[ ]:


automate.make_amazon_build_image("cirrus_amazon_build_image")


# ### Executables
# Here we compile the lambda workers executables.

# In[ ]:


automate.make_executables(
    setup.PUBLISHED_BUILD + "/executables/amazon",
    ("self", "cirrus_amazon_build_image"),
    "ec2-user"
)


# # Cleanup
# ---
# If a cell errors, running this should clean up any resources that were created. After running this cell, the kernel will become unusable and need to be restarted.

# In[ ]:


atexit._run_exitfuncs()


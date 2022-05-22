
# coding: utf-8

# # Logistic Regression
# ---
# This notebook uses Cirrus to run logistic regression on the Criteo dataset.

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
import time


# In[ ]:


# Cirrus produces logs, but they will not show unless we add a handler that prints.
from cirrus import utilities
utilities.set_logging_handler()


# In[ ]:


from cirrus import instance, parameter_server, automate, lr


# ## Instance, server, and task
# ---

# First, we start an EC2 instance.

# In[ ]:


inst = instance.Instance(
    name="lr_example_instance",
    disk_size=32,
    typ="m4.2xlarge",
    username="ubuntu",
    ami_owner_name=("self", "cirrus_server_image")
)
inst.start()


# Second, we create a parameter server to run on our instance.

# In[ ]:


server = parameter_server.ParameterServer(
    instance=inst,
    ps_port=1337,
    error_port=1338,
    num_workers=64
)


# Third, we define our machine learning task.

# In[ ]:


task = lr.LogisticRegression(
    n_workers=16,
    n_ps=1,
    dataset="criteo-kaggle-cirrus",
    learning_rate=0.0001,
    epsilon=0.0001,
    progress_callback=None,
    train_set=(1, 350),
    test_set=(351, 400),
    minibatch_size=25,
    model_bits=19,
    ps=server,
    opt_method="adagrad",
    timeout=60,
    lambda_size=192
)


# ## Run
# ---

# Next, we run our machine learning task.

# In[ ]:


task.run()


# Run this cell to see the present accuracy of the model.

# In[ ]:

c = 0
while c != 60*2:
    for line in server.error_output().split(b'\n')[-10:]:
        if b'Accuracy' in line:
            print(line)
    c += 1
    time.sleep(1)


# ## Cleanup
# ---

# When we're satisfied with the results, we kill our task.

# In[ ]:


task.kill()


# We also need to terminate our instance in order to avoid continuing charges.

# In[ ]:


inst.cleanup()


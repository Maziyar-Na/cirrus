# ## Cleanup
# ---

# When we're satisfied with the results, we kill our task.

# In[ ]:


task.kill()


# We also need to terminate our instance in order to avoid continuing charges.

# In[ ]:


inst.cleanup()

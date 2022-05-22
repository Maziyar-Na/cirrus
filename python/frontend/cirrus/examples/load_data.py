import logging
import sys
from cirrus import utilities
utilities.set_logging_handler()

from cirrus import preprocessing as prep


prep.Preprocessing.load_libsvm('/mnt/serverlessML/lr_example_criteo_ds.svm', 'criteo-kaggle-cirrus')
print("[dbg] Are we lucky to run LR? let's see!")

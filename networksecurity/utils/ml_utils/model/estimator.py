from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import os
import sys

from networksecurity.exception.exceptionfile import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self,model,preprocessor):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def predict(self,x):##any new data prediction
        try:
            x_transform=self.preprocessor.transform(x)
            y_hat=self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException


import os
from pathlib import Path
import pandas as pd 
from src import logger
from sklearn.model_selection import train_test_split

from src.config.configuration import DataTransformationConfig




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def load_data(self)-> pd.DataFrame :
        """
        Load dataset from the configured path.
        """
        try :
            data = pd.read_csv(self.config.data_path)
            logger.info(f"Data loaded successfully from {self.config.data_path}")
            return data
        except Exception as e:
            logger.exception(e)
            raise e
    
    def check_missing_values(self,data : pd.DataFrame):
        """
        Check for missing values and log them.
        """
        missing_values = data.isnull().sum()
        logger.info(f"Missing values per column:\n{missing_values}")
        return missing_values
    
    def generate_summary_statistics(self, data: pd.DataFrame):
        """
        Generate and save summary statistics like mean, median, std, etc.
        """
        
        try :
            summary = data.describe().T
            summary_path = Path(self.config.root_dir,"summary.csv")
            summary.to_csv(summary_path)
            logger.info(f"Summary statistics saved at {summary_path}")
            return summary
        except Exception as e:
            logger.error(f"Error generating summary statistics: {e}")
            raise e
        
    def train_test_split(self, data: pd.DataFrame):
        
        train,test = train_test_split(data,test_size=0.2,random_state=42)
        
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index = False)
        
        logger.info(f"Splitted the data into training and test")
        
        logger.info(train.shape)
        logger.info(test.shape)
        
    
    def perform_full_eda(self):
        """
        Perform full EDA pipeline:
        1. Load data
        2. Check missing values
        3. Generate summary statistics
        4. Detect outliers
        5. Correlation analysis
        """
        logger.info("Starting EDA process...")
        data = self.load_data()
        
        # Step 1: Missing Values
        self.check_missing_values(data)
        
        # Step 2: Summary Statistics
        self.generate_summary_statistics(data)
        
        #step 3: train test split
        
        self.train_test_split(data)
        
        logger.info(f"completed the EDA")
        
        
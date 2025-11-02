import os
import pandas
from src import logger

from src.entity.config_entity import DataValidationConfig


import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self):
        """
        Validate:
        1. If all required columns from schema are present.
        2. If each column has the correct data type.

        Returns:
            bool: True if validation passed, False otherwise.
        """
        try:
            validation_status = True  # Assume valid until proven otherwise

            # Load CSV data
            data = pd.read_csv(self.config.unzip_data_dir)
            data_columns = list(data.columns)
            schema_columns = self.config.all_schema  # Expected schema

            logger.info("Starting column and dtype validation.")

            # Iterate through schema to validate columns
            for col, expected_dtype in schema_columns.items():

                # 1. Check if column exists
                if col not in data_columns:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Failed: Missing column -> {col}\n")
                    logger.error(f"Missing expected column: {col}")
                    return validation_status  # Stop further checks immediately

                # 2. Check if column's dtype matches
                actual_dtype = str(data[col].dtype)
                if actual_dtype != expected_dtype:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(
                            f"Validation Failed: Column '{col}' has dtype '{actual_dtype}', "
                            f"expected '{expected_dtype}'\n"
                        )
                    logger.error(
                        f"Column '{col}' dtype mismatch: expected {expected_dtype}, got {actual_dtype}"
                    )
                    return validation_status  # Stop further checks immediately

            # If all validations pass
            with open(self.config.STATUS_FILE, "w") as f:
                f.write("Validation result: True")

            logger.info("Data validation passed successfully.")
            return validation_status

        except Exception as e:
            logger.exception("An error occurred during data validation.")
            raise e

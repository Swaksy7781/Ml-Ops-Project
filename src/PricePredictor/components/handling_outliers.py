import os
import pandas as pd
from PricePredictor import logger
from PricePredictor.entity.config_entity import OutlierHandlingConfig

class HandlingOutliers:
    def __init__(self, config: OutlierHandlingConfig):
        self.config = config

    def handle_outliers(self):
        """
        Removes outlier data points based on configured IDs.
        """
        try:
            logger.info("Loading processed data for outlier handling...")
            data_path = os.path.join(self.config.input_data_dir, "processed_train.csv") # Input from missing value handling
            df = pd.read_csv(data_path)
            logger.info(f"Data loaded successfully from: {data_path}")

            outlier_ids_to_remove = self.config.outlier_ids
            logger.info(f"Number of outlier IDs to remove: {len(outlier_ids_to_remove)}")

            df = df[~df['Id'].isin(outlier_ids_to_remove)] # Remove rows with specified IDs
            logger.info(f"Outliers removed successfully. Dataframe shape after outlier removal: {df.shape}")

            # Save processed data
            processed_data_path = os.path.join(self.config.processed_data_dir, "processed_train_no_outliers.csv") # New filename
            df.to_csv(processed_data_path, index=False)
            logger.info(f"Processed data (no outliers) saved to: {processed_data_path}")

        except Exception as e:
            logger.exception(e)
            raise e
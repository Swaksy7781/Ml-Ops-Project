import os
import pandas as pd
from PricePredictor import logger
from PricePredictor.entity.config_entity import FeatureEngineeringConfig

class FeatureEngineering:
    def __init__(self, config: FeatureEngineeringConfig):
        self.config = config

    def engineer_features(self):
        """
        Engineers new features based on existing data.
        """
        try:
            logger.info("Loading processed data for feature engineering...")
            data_path = os.path.join(self.config.input_data_dir, "processed_train_no_outliers.csv") # Input from outlier handling
            df = pd.read_csv(data_path)
            logger.info(f"Data loaded successfully from: {data_path}")

            # Feature Engineering
            df['houseage'] = df['YrSold'] - df['YearBuilt']
            df['houseremodelage'] = df['YrSold'] - df['YearRemodAdd']
            df['totalsf'] = df['1stFlrSF'] + df['2ndFlrSF'] + df['BsmtFinSF1'] + df['BsmtFinSF2']
            df['totalarea'] = df['GrLivArea'] + df['TotalBsmtSF']
            df['totalbaths'] = df['BsmtFullBath'] + df['FullBath'] + 0.5 * (df['BsmtHalfBath'] + df['HalfBath'])
            df['totalporchsf'] = df['OpenPorchSF'] + df['3SsnPorch'] + df['EnclosedPorch'] + df['ScreenPorch'] + df['WoodDeckSF']

            logger.info("Features engineered successfully.")

            # Save processed data
            processed_data_path = os.path.join(self.config.processed_data_dir, "processed_train_features.csv") # New filename
            df.to_csv(processed_data_path, index=False)
            logger.info(f"Processed data (with features) saved to: {processed_data_path}")

        except Exception as e:
            logger.exception(e)
            raise e
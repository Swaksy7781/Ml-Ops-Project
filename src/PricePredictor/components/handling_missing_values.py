import os
import pandas as pd
from PricePredictor import logger
from PricePredictor.entity.config_entity import MissingValueHandlingConfig
from sklearn.impute import SimpleImputer


class HandlingMissingValues:
    def __init__(self, config: MissingValueHandlingConfig):
        self.config = config

    def handle_missing_values(self):
        """
        Handles missing values based on the configuration.
        """
        try:
            logger.info("Loading data for missing value handling...")
            data_path = os.path.join(self.config.input_data_dir, "train.csv") # Assuming train.csv is the data file
            df = pd.read_csv(data_path)
            logger.info(f"Data loaded successfully from: {data_path}")

            # Categorical Feature Imputation
            logger.info("Starting categorical feature imputation...")
            cat_config = self.config.categorical_imputation

            for col in cat_config['no_imputation_features']:
                if col in df.columns: # Check if column exists to prevent errors if feature list changes
                    df[col] = df[col].fillna('No')
                    logger.info(f"Imputed missing values in '{col}' with 'No'")

            for col in cat_config['unf_imputation_features']:
                if col in df.columns:
                    df[col] = df[col].fillna('Unf')
                    logger.info(f"Imputed missing values in '{col}' with 'Unf'")

            for col in cat_config['most_frequent_imputation_features']:
                if col in df.columns:
                    most_frequent_category = df[col].mode()[0]  # Get the most frequent category
                    df[col] = df[col].fillna(most_frequent_category)
                    logger.info(f"Imputed missing values in '{col}' of categorical feature with most frequent category: '{most_frequent_category}'")


            # Numerical Feature Imputation
            logger.info("Starting numerical feature imputation...")
            num_config = self.config.numerical_imputation

            for col in num_config['zero_imputation_features']:
                if col in df.columns:
                    df[col] = df[col].fillna(0)
                    logger.info(f"Imputed missing values in '{col}' with 0")

            if ('year_built_imputation_feature' in num_config and num_config['year_built_imputation_feature'] and any(feature in df.columns for feature in num_config['year_built_imputation_feature']) and 'YearBuilt' in df.columns):
                year_built_col = num_config['year_built_imputation_feature']
                df[year_built_col] = df[year_built_col].fillna(df['YearBuilt'])
                logger.info(f"Imputed missing values in '{year_built_col}' with 'YearBuilt'")


            if num_config['general_numerical_mean_imputation']:
                numerical_cols_to_impute = df.select_dtypes(include=['number']).columns.tolist()
                cols_already_imputed = cat_config['no_imputation_features'] + cat_config['unf_imputation_features'] + cat_config['most_frequent_imputation_features'] + num_config['zero_imputation_features']
                if 'year_built_imputation_feature' in num_config and num_config['year_built_imputation_feature']:
                    cols_already_imputed.append(num_config['year_built_imputation_feature'])

                final_numerical_cols_to_impute = [col for col in numerical_cols_to_impute if col not in cols_already_imputed]


                if final_numerical_cols_to_impute:
                    imputer = SimpleImputer(strategy='mean')
                    df[final_numerical_cols_to_impute] = imputer.fit_transform(df[final_numerical_cols_to_impute])
                    logger.info(f"Imputed remaining missing values in numerical features with mean: {final_numerical_cols_to_impute}")
                else:
                    logger.info("No remaining numerical columns to impute with mean.")


            # Save processed data
            processed_data_path = os.path.join(self.config.processed_data_dir, "processed_train.csv")
            df.to_csv(processed_data_path, index=False)
            logger.info(f"Processed data saved to: {processed_data_path}")


        except Exception as e:
            logger.exception(e)
            raise e
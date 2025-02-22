import os
from PricePredictor.constants import *
from PricePredictor.utils.common import read_yaml, create_directories
from PricePredictor.entity.config_entity import (DataIngestionConfig,
                                                    MissingValueHandlingConfig,
                                                    OutlierHandlingConfig) # Import OutlierHandlingConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config


    def get_missing_value_handling_config(self) -> MissingValueHandlingConfig: # New method
        config = self.config.missing_value_handling

        create_directories([config.root_dir,
                            config.processed_data_dir]) # Create processed_data_dir as well

        missing_value_handling_config = MissingValueHandlingConfig(
            root_dir=config.root_dir,
            input_data_dir=config.input_data_dir,
            processed_data_dir=config.processed_data_dir,
            categorical_imputation=config.categorical_imputation,
            numerical_imputation=config.numerical_imputation
        )

        return missing_value_handling_config

    def get_outlier_handling_config(self) -> OutlierHandlingConfig: # New method
        config = self.config.outlier_handling

        create_directories([config.root_dir,
                           config.processed_data_dir])

        outlier_handling_config = OutlierHandlingConfig(
            root_dir=config.root_dir,
            input_data_dir=config.input_data_dir,
            processed_data_dir=config.processed_data_dir,
            outlier_ids=config.outlier_ids
        )

        return outlier_handling_config
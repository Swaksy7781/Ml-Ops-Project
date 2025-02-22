from PricePredictor.config.configuration import ConfigurationManager
from PricePredictor.components.feature_engineering import FeatureEngineering
from PricePredictor import logger

STAGE_NAME = "Feature Engineering stage"

class FeatureEngineeringTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        feature_engineering_config = config.get_feature_engineering_config()
        feature_engineer = FeatureEngineering(config=feature_engineering_config)
        feature_engineer.engineer_features()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = FeatureEngineeringTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
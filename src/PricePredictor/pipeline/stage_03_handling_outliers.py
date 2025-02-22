from PricePredictor.config.configuration import ConfigurationManager
from PricePredictor.components.handling_outliers import HandlingOutliers
from PricePredictor import logger

STAGE_NAME = "Handling Outliers stage"

class OutlierHandlingTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        outlier_handling_config = config.get_outlier_handling_config()
        outlier_handler = HandlingOutliers(config=outlier_handling_config)
        outlier_handler.handle_outliers()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = OutlierHandlingTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
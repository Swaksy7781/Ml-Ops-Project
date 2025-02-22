from PricePredictor.config.configuration import ConfigurationManager
from PricePredictor.components.handling_missing_values import HandlingMissingValues
from PricePredictor import logger


STAGE_NAME = "Handling Missing Values stage"

class MissingValueHandlingTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        missing_value_handling_config = config.get_missing_value_handling_config()
        missing_value_handler = HandlingMissingValues(config=missing_value_handling_config)
        missing_value_handler.handle_missing_values()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = MissingValueHandlingTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
from PricePredictor import logger
from PricePredictor.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from PricePredictor.pipeline.stage_02_handling_missing_values import MissingValueHandlingTrainingPipeline
from PricePredictor.pipeline.stage_03_handling_outliers import OutlierHandlingTrainingPipeline # Import new stage

# from PricePredictor.pipeline.stage_03_model_trainer import ModelTrainingPipeline
# from PricePredictor.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Handling Missing Values stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = MissingValueHandlingTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Handling Outliers stage" # Define stage name for new stage
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = OutlierHandlingTrainingPipeline() # Instantiate and run new stage
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# STAGE_NAME = "Prepare base model"
# try:
#    logger.info(f"*******************")
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    prepare_base_model = PrepareBaseModelTrainingPipeline()
#    prepare_base_model.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e




# STAGE_NAME = "Training"
# try:
#    logger.info(f"*******************")
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    model_trainer = ModelTrainingPipeline()
#    model_trainer.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e





# STAGE_NAME = "Evaluation stage"
# try:
#    logger.info(f"*******************")
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    model_evalution = EvaluationPipeline()
#    model_evalution.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

# except Exception as e:
#         logger.exception(e)
#         raise e
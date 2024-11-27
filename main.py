from cnnclassifier import logger
from cnnclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnclassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main() 
    logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
except Exception as e:
    logger.exception(e)
    raise e
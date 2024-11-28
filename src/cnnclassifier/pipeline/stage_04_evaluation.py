from cnnclassifier.config.configuration import ConfigurationManager
from cnnclassifier.components.evaluation import Evaluation
from cnnclassifier import logger


STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass
     
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f" <<<<<----- {STAGE_NAME} started ----->>>>> ")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f" ----->>>>> {STAGE_NAME} completed <<<<<----- ")
    except Exception as e:
        logger.exception(e)
        raise e
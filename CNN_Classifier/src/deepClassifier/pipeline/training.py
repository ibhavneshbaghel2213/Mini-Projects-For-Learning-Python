from deepClassifier.config import ConfigurationManager
from deepClassifier import logger
from deepClassifier.components.prepare_callback import PrepareCallback
from deepClassifier.components.Training_stage import Training



STAGE_NAME= "Preparing Call Back and Training stage started..."


def main():
    config = ConfigurationManager()
    prepare_callback_config= config.get_prepare_call_back()
    prepare_callback= PrepareCallback(config=prepare_callback_config)
    callback_list=  prepare_callback.get_tb_ckpt_callbacks()

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(
        callback_list=callback_list
    )



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
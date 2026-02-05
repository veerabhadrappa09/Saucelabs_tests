import logging

class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\saucelabs.log",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



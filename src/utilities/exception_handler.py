import logging
import sys


class ExceptionHandler:
    def __init__(self, log_file):
        """Initialize the exception handler and configure the logging system."""

        self.log_file = log_file
        self.setup_logging()

    def setup_logging(self):
        """Configure the logging system."""

        logging.basicConfig(filename=self.log_file,
                            level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def log_exception(self, exception_type, message):
        """Log the exception to the log file."""

        if exception_type in [Exception, ValueError, FileNotFoundError]:
            logging.exception(message)

        elif exception_type in [KeyboardInterrupt, EOFError, RuntimeError]:
            print('Stop')
            sys.exit()

        else:
            print(f'[!] Error saved in file error_log.txt. ({exception_type})')
            logging.error(message)
""" This module contains a Logger class that is used for logging throughout the project """

import logging
import os
import datetime


class Logger(logging.Logger):
    """ This class is used to initialize the logger and handle logging """

    def __init__(self, name: str = '', log_to_file=False, log_level=logging.INFO):
        # Initialize the logger
        super().__init__(name)
        self.setLevel(log_level)

        # Define the log message format
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if log_to_file:
            # Create a logs directory if one doesn't exist
            if not os.path.exists('logs'):
                os.makedirs('logs')

            # Generate a log file name based on the current date and time
            log_file = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

            # Combine the log directory and file name to get the full log file path
            log_file_path = os.path.join('logs', log_file)

            # Create a file handler that writes log messages to a file
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)

        # Create a console handler to also display log messages in the console
        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.addHandler(console_handler)
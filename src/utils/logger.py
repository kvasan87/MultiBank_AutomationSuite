import logging
import os
import sys
from pathlib import Path
from datetime import datetime


class Logger:
    """Centralized logging manager"""

    _logger = None
    _log_file = None

    @classmethod
    def setup_logging(cls, log_level=logging.INFO, log_dir="logs"):
        """
        Setup logging configuration

        Args:
            log_level: Logging level (default: INFO)
            log_dir: Directory to store log files
        """
        # Create logs directory
        log_path = Path(log_dir)
        log_path.mkdir(exist_ok=True)

        # Create log filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        cls._log_file = log_path / f"test_run_{timestamp}.log"

        # Create logger
        cls._logger = logging.getLogger(__name__)
        cls._logger.setLevel(log_level)

        # Clear existing handlers
        cls._logger.handlers.clear()

        # File handler - UTF-8 encoding for cross-platform compatibility
        try:
            file_handler = logging.FileHandler(
                cls._log_file,
                encoding='utf-8',
                mode='w'
            )
            file_handler.setLevel(log_level)
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            cls._logger.addHandler(file_handler)
        except Exception as e:
            print(f"Error setting up file handler: {e}")

        # Console handler - with encoding fallback for Windows
        try:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(log_level)

            # Use UTF-8 encoding, fallback to system default if needed
            if hasattr(console_handler.stream, 'reconfigure'):
                # Python 3.7+
                console_handler.stream.reconfigure(encoding='utf-8', errors='replace')

            console_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            console_handler.setFormatter(console_formatter)
            cls._logger.addHandler(console_handler)
        except Exception as e:
            print(f"Error setting up console handler: {e}")

    @classmethod
    def get_logger(cls):
        """Get the logger instance"""
        if cls._logger is None:
            cls.setup_logging()
        return cls._logger

    @classmethod
    def get_log_file(cls):
        """Get the log file path"""
        return cls._log_file


def log_info(message):
    """Log info level message"""
    logger = Logger.get_logger()
    # Remove special characters that might cause encoding issues
    safe_message = str(message).encode('utf-8', errors='replace').decode('utf-8')
    logger.info(safe_message)


def log_debug(message):
    """Log debug level message"""
    logger = Logger.get_logger()
    safe_message = str(message).encode('utf-8', errors='replace').decode('utf-8')
    logger.debug(safe_message)


def log_warning(message):
    """Log warning level message"""
    logger = Logger.get_logger()
    safe_message = str(message).encode('utf-8', errors='replace').decode('utf-8')
    logger.warning(safe_message)


def log_error(message):
    """Log error level message"""
    logger = Logger.get_logger()
    safe_message = str(message).encode('utf-8', errors='replace').decode('utf-8')
    logger.error(safe_message)


def log_critical(message):
    """Log critical level message"""
    logger = Logger.get_logger()
    safe_message = str(message).encode('utf-8', errors='replace').decode('utf-8')
    logger.critical(safe_message)
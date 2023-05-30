from loguru import logger
from . import settings
import os


def logger_init() -> None:
	if not os.path.exists('loguru_logging'):
		os.mkdir('loguru_logging')  # need for it if compiled version of program will be used
	for level in settings.LOGGING_LEVELS:
		logger.add(
			settings.ERRORS_OUTPUT_FILE,
			level=level,
			format=settings.LOGGING_FORMAT,
			rotation="1 MB",
			compression="zip"
		)


def stderror(exception: Exception) -> None:
	logger.error(
		exception.__class__.__name__, exception.with_traceback(exception.__traceback__)
	)

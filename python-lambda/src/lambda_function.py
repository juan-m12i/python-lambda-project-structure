# -*- coding: utf-8 -*-

from functools import reduce
import datetime
from dateutil.tz import tzutc
import os
import json
import logging

import aws_helper
import helper_functions as hf


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

localAwsConfig = aws_helper.LocalAwsConfig()
awsHelper = localAwsConfig.get_helper()




def handler() -> dict:
    """Core function
    """
    try:
        print("handler")

    except Exception as e:
        logger.error(e)
        raise e


class ErrorParsingLambdaEvent(Exception):
    pass


def get_object_details_from_event(event: dict) -> dict:
    """Parses AWS "Create S3 Object" event trigger

    Args:
        event: Dictionary with information about the event that triggered

    Returns:
        TBD

    Raises:
        ErrorParsingLambdaEvent: TBC
    """
    try:
        data = {}

        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

        error_messages = []
        if 1 == 2:
            error_messages.append("Example Error")

        deal_with_errors(error_messages)
        return data
    except Exception as e:
        error_message = "Error when processing AWS lambda's event to get the S3 object"
        logger.error(e)
        logger.error(error_message)
        logger.error(json.dumps(event))
        raise ErrorParsingLambdaEvent(error_message)


def lambda_handler(event: object, context: object) -> str:
    """ Main Code

    Args:
        event: Dictionary with information about the event that triggered
        aws lambda execution as per aws specification
        context: Dictionary as per aws lambda specification

    Returns:
        "OK"
    """
    try:
        data = get_data_from_event(event)
        identity(context)
        return handler()
    except ErrorParsingLambdaEvent as e:
        raise e
    except Exception as e:
        logger.error(e)
        logger.error("Error in lambda_handler")
        raise e


def local_handler():
    """Runs the function from a local context
    """
    try:
        handler()
    except Exception as e:
        logger.error(e)
        raise e
    else:
        return "OK"


if __name__ == '__main__':
    local_handler()


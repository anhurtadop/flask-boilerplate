"""IndexController"""
# pylint: disable=too-few-public-methods
import logging
from flask import Response

from ..utils.response_util import ResponseUtil
from ..messages import messages as msg


class IndexController:
    """IndexController"""
    logger = logging.getLogger(__name__)

    def index(self) -> Response:
        """index"""
        try:
            return ResponseUtil.json(None, 200, msg["general"]["index"], None)
        except Exception as ex:
            self.logger.error(str(ex))
            return ResponseUtil.json(None, 500, msg["general"]["error_500"], str(ex))

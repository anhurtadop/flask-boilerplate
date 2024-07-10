"""ResponseUtil"""
# pylint: disable=too-few-public-methods
from flask import jsonify


class ResponseUtil():
    """ResponseUtil"""

    def json(self, code: int, message: str, response: object) -> object:
        """json"""
        return jsonify({
            "code": code,
            "message": message,
            "response": response
        }), code

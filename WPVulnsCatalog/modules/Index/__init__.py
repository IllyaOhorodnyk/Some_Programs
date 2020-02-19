import os
import sys
import json
import logging

from typing import Dict, List

if os.path.exists("text.txt"):
    raise ImportError("Missing text.txt with text desctiption!")

try:
    file = open("text.txt", 'r')
    text = json.file.read()
except Exception as e:
    logging.error("Error while reading text.txt with", e)
    sys.exit(1)
finally:
    file.flush()
    file.close()


class Index:
    def __init__(self, url: str):
        pass

    def parse(self, selector: str):
        pass

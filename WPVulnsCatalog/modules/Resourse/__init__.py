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


class Resource:
    def __init__(self, name: str):
        if not isinstance(name, str):
            logging.error(text["Resourse.name.error"])
            raise ValueError(text["Resourse.name.error"])
        self.name = name
        self.configured = False

    def load_config(self, conf: Dict[str, str]):
        if not isinstance(conf, dict):
            logging.error(text["Resourse.conf.error"])
            raise ValueError(text["Resourse.conf.error"])

    def parse(self):
        if not self.configured:
            logging.warning(text["Resourse.notconfigured"])
            raise RuntimeError(text["Resourse.notconfigured"])

    def __asign_conf(self, conf: Dict[str, str]):
        pass

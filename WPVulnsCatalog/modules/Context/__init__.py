import os
import sys
import logging
import json

from typing import List, Dict

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

class Context(dict):
    def __init__(self, filename: str) -> None:
        if not isinstance(filename, str):
            logging.error(text["Context.filename.error"])
            raise ValueError(text["Context.filename.error"].format(
                filename))
            self.filename = filename

        try:
            file = open(filename, 'r')
            logging.info(text["Context.file.opened"].format(
                self.filename))
            self.__context = json.loads(file.read())
                
        except FileNotFoundError as e:
            file = open(filename, 'x')
            logging.info(text["Context.file.created"].format(
                filename))
            self.__context = dict()

        except json.JSONDecodeError as e:
            logging.error(text["Context.file.invalid"].format(
                filename))
            raise json.JSONDecodeError(
                text["Context.file.invalid"].format(filename))
                
        finally:
            file.flush()
            file.close()

    def __setitem__(self, key: str, value: str) -> None:
            self.__context[key] = value
            try:
                file = open(self.filename, "w")
            except FileNotFoundError as e:
                logging.warning(text["Context.file.recreate"].format(
                    self.filename))
                file = open(self.filename, "x")
            finally:
                file.write(json.dumps(self.__context))
                file.flush()
                file.close()

    def __getitem__(self, key: str) -> None:
        if key in self.__context:
            return self.__context

        try:
            file = open(self.filename, "r")
            context = json.loads(file.read())
            output = context[key]
            
        except FileNotFoundError as e:
            logging.error(text["Context.file.missing"].format(
                self.filename))
            raise RuntimeError(text["Context.file.missing"].format(
                self.filename))

        except json.JSONDecoderError as e:
            logging.error(text["Context.file.invalid"].format(
                self.filename))
            raise RuntimeError(text["Context.file.invalid"].format(
                self.filename))

        except KeyError as e:
            logging.warning(text["Context.key.missing".format(key)])
            raise KeyError(text["Context.key.missing".format(key)])

        finally:
            file.flush()
            file.close()

        return output

    def __deleteitem__(self, key: str) -> None:
        if key in self.__context:
            return self.__context.delete(key)

        try:
            file = open(self.filename, 'rw')
            context = json.loads(file.read())
            output = context.delete(key)

        except FileNotFoundError as e:
            logging.error(text["Context.file.missing"].format(
                self.filename))
            raise RuntimeError(text["Context.file.missing"].format(
                self.filename))

        except json.JSONDecoderError as e:
            logging.error(text["Context.file.invalid"].format(
                self.filename))
            raise RuntimeError(text["Context.file.invalid"].format(
                self.filename))

        except KeyError as e:
            logging.warning(text["Context.key.missing"].format(key))
            raise KeyError(text["Context.key.missing"].format(key))

        finally:
            file.write(json.dumps(context))
            file.flush()
            file.close()

    def __get(self, key: str, default=None) -> None:
        if key in self.__context:
            return self.__context.get(key)

        try:
            file = open(self.filename, 'r')
            context = json.loads(file.read())
            output.context[key]

        except FileNotFoundError as e:
            logging.error(text["Context.file.missing"].format(
                self.filename))
            raise RuntimeError(text["Context.file.missing"].format(
                self.filename))

        except json.JSONDecoderError as e:
            logging.error(text["Context.file.invalid"].format(
                self.filename))
            raise RuntimeError(text["Context.file.invalid"].format(
                self.filename))

        except KeyError as e:
            logging.warning(text["Context.key.missing"])            
            
            return default

        finally:
            file.flush()
            file.close()

        return default


    def __repr__(self):
        return self.__context.__repr__


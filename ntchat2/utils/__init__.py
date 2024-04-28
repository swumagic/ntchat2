import os
import subprocess
import uuid
import time
from typing import (
    Any,
    Dict
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

WC_DIR = os.path.join(BASE_DIR, "wc")

class ObjectDict(Dict[str, Any]):
    """Makes a dictionary behave like an object, with attribute-style access.
    """

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value


def generate_guid(prefix=''):
    return str(uuid.uuid3(uuid.NAMESPACE_URL, prefix + str(time.time())))


def fake_wechat_version(pid, old_version, new_version):
    return subprocess.run([os.path.join(os.path.join(BASE_DIR, "wc"), "faker.exe"), str(pid), old_version, new_version], stdout=subprocess.DEVNULL).returncode

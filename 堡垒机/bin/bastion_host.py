# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import os
import sys

# 未实现：以后实现

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

from models import models
from conf import settings

if __name__ == "__main__":
    from modules.actions import excute_from_command_line
    excute_from_command_line(sys.argv)
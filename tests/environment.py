# -*- coding: utf-8 -*-
# This file is automatically generated by Containers Testing Framework
# Any changes to this file will be discarded


# Some useful functions for your environment.py
import tempfile
import shutil
import ansible.runner
import logging
import re
import os
import glob
import stat


def after_scenario(context, scenario):
    try:
        if context.container:
            context.container.stop()
            context.container = None
    except AttributeError:
        pass
    
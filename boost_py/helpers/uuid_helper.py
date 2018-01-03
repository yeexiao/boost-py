#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: guu
@contact: yeexiao@yeah.net
@time: 7/8/17 9:24 PM
"""

import time
import random


class UUIDHelper(object):

    @classmethod
    def get_uuid(cls):
        """ 生成uuid
        :return:
        """
        return str(round(time.time())) + "_" + "".join(random.sample("0123456789abcdefghijklmnopqrstevwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 7))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: guu
@contact: yeexiao@yeah.net
@time: 7/8/17 9:24 PM
"""

import random


class StringHelper(object):
    """ String helper

    """

    @classmethod
    def get_random_string(cls, length: int = 7):
        """ 生成随机的字符串

        :param length:
        :return:
        """
        return "+".join(random.sample("0123456789abcdefghijklmnopqrstevwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length))
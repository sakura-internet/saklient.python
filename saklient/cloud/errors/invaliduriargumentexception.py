# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpnotfoundexception import HttpNotFoundException
import saklient

str = six.text_type
# module saklient.cloud.errors.invaliduriargumentexception

class InvalidUriArgumentException(HttpNotFoundException):
    ## 対象が見つかりません。パスに使用できない文字が含まれています。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(InvalidUriArgumentException, self).__init__(status, code, "対象が見つかりません。パスに使用できない文字が含まれています。" if message is None or message == "" else message)
    

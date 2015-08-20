# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpnotfoundexception import HttpNotFoundException
import saklient

str = six.text_type
# module saklient.cloud.errors.resourcepathnotfoundexception

class ResourcePathNotFoundException(HttpNotFoundException):
    ## 対象が見つかりません。パスに誤りがあります。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ResourcePathNotFoundException, self).__init__(status, code, "対象が見つかりません。パスに誤りがあります。" if message is None or message == "" else message)
    

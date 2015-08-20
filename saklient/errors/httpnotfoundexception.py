# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .httpexception import HttpException
import saklient

str = six.text_type
# module saklient.errors.httpnotfoundexception

class HttpNotFoundException(HttpException):
    ## 対象が見つかりません。対象は利用できない状態か、IDまたはパスに誤りがあります。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpNotFoundException, self).__init__(status, code, "対象が見つかりません。対象は利用できない状態か、IDまたはパスに誤りがあります。" if message is None or message == "" else message)
    

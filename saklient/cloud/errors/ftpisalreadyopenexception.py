# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.ftpisalreadyopenexception

class FtpIsAlreadyOpenException(HttpConflictException):
    ## 要求された操作を行えません。FTP共有は既に開始されています。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(FtpIsAlreadyOpenException, self).__init__(status, code, "要求された操作を行えません。FTP共有は既に開始されています。" if message is None or message == "" else message)
    

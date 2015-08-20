# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpforbiddenexception import HttpForbiddenException
import saklient

str = six.text_type
# module saklient.cloud.errors.dontcreateinsandboxexception

class DontCreateInSandboxException(HttpForbiddenException):
    ## 要求された操作は許可されていません。ゾーンをまたぐ一部のリソースは課金対象です。料金をご確認の上、他のゾーンで作成してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DontCreateInSandboxException, self).__init__(status, code, "要求された操作は許可されていません。ゾーンをまたぐ一部のリソースは課金対象です。料金をご確認の上、他のゾーンで作成してください。" if message is None or message == "" else message)
    

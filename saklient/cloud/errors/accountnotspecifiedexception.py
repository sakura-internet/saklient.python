# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpforbiddenexception import HttpForbiddenException
import saklient

str = six.text_type
# module saklient.cloud.errors.accountnotspecifiedexception

class AccountNotSpecifiedException(HttpForbiddenException):
    ## 要求された操作は許可されていません。このAPIはアカウントを特定できる認証方法でアクセスする必要があります。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AccountNotSpecifiedException, self).__init__(status, code, "要求された操作は許可されていません。このAPIはアカウントを特定できる認証方法でアクセスする必要があります。" if message is None or message == "" else message)
    

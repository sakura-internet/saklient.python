# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.disklicensemismatchexception

class DiskLicenseMismatchException(HttpConflictException):
    ## 要求された操作を行えません。ライセンスの問題により、組み合わせて使用できないディスクが接続されています。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DiskLicenseMismatchException, self).__init__(status, code, "要求された操作を行えません。ライセンスの問題により、組み合わせて使用できないディスクが接続されています。" if message is None or message == "" else message)
    

import util.open_util
class BaseClient():
    """基础的参数类"""

    def __new__(self,applicationkey,applicationSecret,authenticator):
        """初始化基础的参数"""
        #实例化对象
        openPlateform = util.open_util.OpenPlatform()
        openPlateform.asecret = applicationSecret
        #print(openPlateform.asecret)
        openPlateform.sign_dict["_akey"] = applicationkey
        openPlateform.headers['authenticator'] = authenticator
        return openPlateform

    def initBaseClient(applicationkey,applicationSecret,authenticator):
        return BaseClient(applicationkey,applicationSecret,authenticator);

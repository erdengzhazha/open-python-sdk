import group.openplatform_base.openplatform_base_const
import time
class ApiOpenplatformBase():
    """开放平台人脸基础数据API"""
    def __init__(self,openPlateform):
        self.open = openPlateform

    def getStores(self,orgid,version = 'v1'):
        """获取门店列表"""
        params = {
            "orgid" : orgid,
            "_version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.openplatform_base.openplatform_base_const.OpenplatformBase.open_openplatform_base_getStores
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def getUsers(self,orgid,depId,stime,etime,version = 'v1'):
        """获取用户列表"""
        params = {
            "orgid" : orgid,
            "depId" : depId,
            "stime" : stime,
            "etime" : etime,
            "version" : version,
            "_timestamp" : time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())),
            "_mt" : group.openplatform_base.openplatform_base_const.OpenplatformBase.open_openplatform_base_getUsers
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getAgeData(self,orgid,depId,stime,etime,version = 'v1'):
        """获取人脸客流年龄分布"""
        params = {
             "orgid" : orgid,
             "depId" : depId,
             "stime" : stime,
             "etime" : etime,
             "version" : version,
             "_timestamp" : time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())),
             "_mt" : group.openplatform_base.openplatform_base_const.OpenplatformBase.open_openplatform_base_getAgeData
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getGenderData(self,orgid,depId,stime,etime,version = 'v1'):
        """获取人脸客流性别分布"""
        params = {
            "orgid": orgid,
            "depId": depId,
            "stime": stime,
            "etime": etime,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.openplatform_base.openplatform_base_const.OpenplatformBase.open_openplatform_base_getGenderData
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getDeviceLatestPhotos(self,orgid,device_mac,size,version = 'v1'):
        """获取设备最新抓拍的照片"""
        params = {
            "orgid" : orgid,
            "device_mac" : device_mac,
            "size" : size,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.openplatform_base.openplatform_base_const.OpenplatformBase.open_openplatform_base_getDeviceLatestPhotos
        }
        self.open.createSign(params)
        return self.open.httpRequest()
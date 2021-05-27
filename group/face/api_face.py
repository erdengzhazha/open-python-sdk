import group.face.face_const
import time
class ApiFace():
    """开放平台人脸api"""

    def __init__(self,openPlateform):
        """构造方法"""
        self.open = openPlateform;

    def addUser(self,DataUser,version='v1'):
        """注册人脸"""
        params = {
            "DataUser" : DataUser,
            "version ": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_addUser
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def queryUserCallBack(self,thirdpicurl,wdzpicurl,username,userid,memberType,gender,age,glass,emotion,ethnicity,skinstatus,arriveTime,groupid,orgid,deviceId,deviceMac,deviceName,faceId,version='v1'):
        """抓拍回调"""
        params = {
            "thirdpicurl" : thirdpicurl,
            "wdzpicurl" : wdzpicurl,
            "username" : username,
            "userid" : userid,
            "memberType" : memberType,
            "gender" : gender,
            "age" : age,
            "glass" : glass,
            "emotion" : emotion,
            "ethnicity" : ethnicity,
            "skinstatus" : skinstatus,
            "arriveTime" : arriveTime,
            "groupid" : groupid,
            "orgid" : orgid,
            "deviceId" : deviceId,
            "deviceMac" : deviceMac,
            "deviceName" : deviceName,
            "faceId" : faceId,
            "version " : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_queryUserCallBack
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def addGroup(self,groupname,orgid,version='v1'):
        """添加分组"""
        params = {
            "groupname" : groupname,
            "orgid" : orgid,
            "version" : version,
            "_timestamp" : time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_addGroup
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def queryGroup(self,orgid,version = 'v1'):
        """查询分组"""
        params = {
            "orgid" : orgid,
            "version" : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_queryGroup
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def queryDevice(self,orgid,groupid,deviceMac,version='v1'):
        """查询人脸设备"""
        params = {
            "orgid" : orgid,
            "groupid" : groupid,
            "deviceMac" : deviceMac,
            "version" :version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_queryDevice
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def bindingDevice(self,orgid,groupid,deviceId,version = 'v1'):
        """绑定人脸设备"""
        params = {
            "orgid" : orgid,
            "groupid" : groupid,
            "deviceId" : deviceId,
            "version" :version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_queryDevice
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def updateUser(self,orgid,departno,userid,thirdpicurl,username,memberType,mobilephone,gender,checkrepeat,version = 'v1'):
        """更新人脸"""
        params = {
            "orgid":orgid,
            "departno":departno,
            "userid":userid,
            "thirdpicurl":thirdpicurl,
            "username":username,
            "memberType":memberType,
            "mobilephone":mobilephone,
            "gender":gender,
            "checkrepeat": checkrepeat,
            "version" :version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_updateUser
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def addUser(self,orgid,departno,userid,thirdpicurl,username,memberType,mobilephone,gender,checkrepeat,cardNumber,version = 'v1'):
        """单个用户注册人脸用户至万店掌人脸平台"""
        params = {
            "orgid" : orgid,
            "departno" : departno,
            "userid" : userid,
            "thirdpicurl" : thirdpicurl,
            "username" : username,
            "memberType" : memberType,
            "mobilephone" : mobilephone,
            "gender" : gender,
            "checkrepeat" : checkrepeat,
            "cardNumber" : cardNumber,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_addUser
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def deleteUser(self,orgid,departno,userid,version = 'v1'):
        """删除用户所有人脸集合"""
        params = {
            "orgid" : orgid,
            "departno" : departno,
            "userid" : userid,
            "version" : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_deleteUser
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def addFaceUrl(self,orgid,departno,userid,thirdpicurl,version = 'v1' ):
        """给某个用户添加一张人脸照片"""
        params = {
            "orgid" : orgid,
            "departno" : departno,
            "userid" : userid,
            "thirdpicurl" : thirdpicurl,
            "version" : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_addFaceUrl
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def updateFaceUrl(self,orgid,departno,userid,thirdpicurl,faceid,version = 'v1'):
        """根据三方用户编号及人脸编号更新人脸照片"""
        params = {
            "orgid" : orgid,
            "departno" : departno,
            "userid" : userid,
            "thirdpicurl" : thirdpicurl,
            "faceid" : faceid,
            "version" : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_updateFaceUrl
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def deleteFaceUrl(self,orgid,departno,userid,faceid,version  = 'v1'):
        """根据三方用户编号和人脸照片编号删除指定人脸照片"""
        params = {
            "orgid" : orgid,
            "departno" : departno,
            "userid" : userid,
            "faceid" : faceid,
            "version" : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_deleteFaceUrl
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def getFaceUrls(self,orgid,departno,userid,version = 'v1'):
        """根据三方会员编号获取所有的人脸照片信息"""
        params = {
            "orgid" : orgid,
            "departno" : departno,
            "userid" : userid,
            "version" : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_getFaceUrls
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def getDeviceGroupsConfig(self,orgid,deviceMac,version = 'v1'):
        """查询设备多分组场景配置"""
        params = {
            "orgid" : orgid,
            "deviceMac" : deviceMac,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_getDeviceGroupsConfig
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def addDeviceGroup(self,orgid,groupid,deviceMac,version = 'v1'):
        """添加设备分组配置"""
        params = {
            "orgid" : orgid,
            "groupid" : groupid,
            "deviceMac" : deviceMac,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_addDeviceGroup
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def updateDeviceGroup(self,orgid,groupid,groupid2,deviceMac,version = 'v1'):
        """更新设备分组配置"""
        params = {
            "orgid" : orgid,
            "groupid" : groupid,
            "groupid2" : groupid2,
            "deviceMac" : deviceMac,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_updateDeviceGroup
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def deleteDeviceGroup(self,orgid,groupid,deviceMac,version = 'v1'):
        """删除设备分组配置"""
        params = {
            "orgid" : orgid,
            "groupid" : groupid,
            "deviceMac" : deviceMac,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_deleteDeviceGroup
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def serchGroupUser(self,orgid,groupid,thirdpicurl,threshold,version = 'v1'):
        """根据照片搜索指定分组内用户"""
        params = {
            "orgid" : orgid,
            "groupid" : groupid,
            "thirdpicurl" : thirdpicurl,
            "threshold" : threshold,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_serchGroupUser
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def detect(self,url,version = 'v1'):
        """人脸检测"""
        params = {
            "url" : url,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.face.face_const.FaceConst.method_open_face_detect
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result
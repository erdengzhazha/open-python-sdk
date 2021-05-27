import group.shopweb_thirdparty_face.shopweb_thirdparty_face_const
import time
class ApiShopwebThirdpartyFace():

    def __init__(self,openPlateform):
        self.open = openPlateform

    def registerVip(self,imageUrl,depid,useid,orgid,faceId,username,mobilephone,cardNumber,gender,version = 'v1'):
        """开发者平台注册用户至万店掌人脸平台（需要faceId）"""
        params = {
            "imageUrl" : imageUrl,
            "depid" : depid,
            "useid" : useid,
            "orgid" : orgid,
            "faceId" : faceId,
            "username" : username,
            "mobilephone" : mobilephone,
            "cardNumber" : cardNumber,
            "gender" : gender,
            "version" : version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_registerVip
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getFaceCustomer(self,depid,deviceMac,orgid,starttime,endtime,version = 'v1'):
        """获取设备列表数据接口"""
        params = {
            "depid" : depid,
            "deviceMac" : deviceMac,
            "orgid" : orgid,
            "starttime" : starttime,
            "endtime" : endtime,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getFaceCustomer
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def queryUserCallBack(self,version = 'v1'):
        """人脸数据推送  版本推荐v2"""
        params = {
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_queryUserCallBack
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getFaceCustomerList(self,depid,deviceMac,orgid,starttime,endtime,pageNumber,pageSize,version  = 'v1'):
        """获取设备抓拍数据"""
        params = {
            "depid" : depid,
            "deviceMac" : deviceMac,
            "orgid" : orgid,
            "starttime" : starttime,
            "endtime" : endtime,
            "pageNumber" : pageNumber,
            "pageSize" : pageSize,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getFaceCustomerList
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getSnapshotOnDevice(self,mac,orgid,version  = 'v1'):
        """实际场景抓拍"""
        params = {
            "mac" : mac,
            "orgid" : orgid,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getSnapshotOnDevice
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def updateVip(self,errorFaceId,depid,orgid,imageUrl,userid,userName,memberType,mobilePhone,cardNumber,gender,faceId,version = 'v1'):
        """修改会员接口"""
        params = {
            "errorFaceId" : errorFaceId,
            "depid" : depid,
            "orgid" : orgid,
            "imageUrl" : imageUrl,
            "userid" : userid,
            "userName" : userName,
            "memberType" : memberType,
            "mobilePhone" : mobilePhone,
            "cardNumber" : cardNumber,
            "gender" : gender,
            "faceId" : faceId,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_updateVip
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getPosFaceCustomerList(self,depId,gender,minAge,maxAge,startDateStr,endDateStr,content,regType,mac,pageNum,pageSize,version = 'v1'):
        """获取人脸追溯数据"""
        params = {
            "depId" : depId,
            "gender" : gender,
            "minAge" : minAge,
            "maxAge" : maxAge,
            "startDateStr" : startDateStr,
            "endDateStr" : endDateStr,
            "content" : content,
            "regType" : regType,
            "mac" : mac,
            "pageNum" : pageNum,
            "pageSize" : pageSize,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getPosFaceCustomerList
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def updateFaceCustomerRemark(self,faceCustomerId,remark,groupId,version = 'v1'):
        """修改人脸追溯会员备注"""
        params = {
            "faceCustomerId" : faceCustomerId,
            "remark" : remark,
            "groupId" : groupId,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_updateFaceCustomerRemark
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def searchUser(self,orgid,depid,imageUrl,version = 'v1'):
        """搜索企业门店下指定用户"""
        params = {
            "orgid" : orgid,
            "depid" : depid,
            "imageUrl" : imageUrl,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_searchUser
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def registerVip(self,imageUrl,depid,useid,orgid,username,mobilephone,cardNumber,gender,memberType,version = 'v1'):
        """注册人脸（不需要faceId）"""
        params = {
            "imageUrl" : imageUrl,
            "depid" : depid,
            "useid" : useid,
            "orgid" : orgid,
            "username" : username,
            "mobilephone" : mobilephone,
            "cardNumber" : cardNumber,
            "gender" : gender,
            "memberType" : memberType,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_registerVip
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getFaceCustomerList(self,depid,deviceMac,orgid,starttime,endtime,pageNumber,pageSize,version = 'v1'):
        """获取设备抓拍数据"""
        params = {
            "depid" : depid,
            "deviceMac" : deviceMac,
            "orgid" : orgid,
            "starttime" : starttime,
            "endtime" : endtime,
            "pageNumber" : pageNumber,
            "pageSize" : pageSize,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getFaceCustomerList
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getDepCustomerAgeReport(self,orgid,depid,starttime,endtime,version = 'v1'):
        """获取年龄分布"""
        params = {
            "orgid" : orgid,
            "depid" : depid,
            "starttime" : starttime,
            "endtime" : endtime,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getDepCustomerAgeReport
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getDepCustomerGenderReport(self,orgid,depid,starttime,endtime,version = 'v1'):
        """获取性别分布"""
        params = {
            "orgid" : orgid,
            "depid" : depid,
            "starttime" : starttime,
            "endtime" : endtime,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getDepCustomerGenderReport
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getVipList(self,orgid,starttime,endtime,version = 'v1'):
        """获取企业下的会员列表"""
        params = {
            "orgid" : orgid,
            "starttime" : starttime,
            "endtime" : endtime,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getVipList
        }
        self.open.createSign(params)
        return self.open.httpRequest()

    def getBatchFlowData(self,startTime,endTime,depId,orgId,version = 'v1'):
        """批次接口数据接口"""
        params = {
            "startTime" : startTime,
            "endTime" : endTime,
            "depId" : depId,
            "orgId" : orgId,
            "version": version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt": group.shopweb_thirdparty_face.shopweb_thirdparty_face_const.ShopwebThirdpartyFaceConst.open_shopweb_thirdparty_face_getBatchFlowData
        }
        self.open.createSign(params)
        return self.open.httpRequest()
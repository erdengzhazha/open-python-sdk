import group.gateway.gateway_const
import time
class ApiGateway():
    """权限API组"""
    def __init__(self,openPlateform):
        """构造方法"""
        self.open = openPlateform;

    def authentication(self,orgid,version="v1"):
        """根据组织机构代码获取开发者账号详细信息"""
        # 请求参数
        params = {
            # 开放平台企业id
            "orgid":orgid,
            # 默认版本v1 推荐版本v2
            "_version":version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_gateway_authentication
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def getBusinessOrg(self,orgid,version="v1"):
        """获取业务平台组织机构列表"""
        # 请求参数
        params = {
            # 开放平台企业id
            "orgid":orgid,
            # 默认版本为 v1
            "_version":version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_gateway_getBusinessOrg
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def getRoleListByGroup(self,version="v1"):
        """获取企业下所有角色"""
        # 请求参数
        params = {
            # 默认版本v1
            "_version":version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_shopweb_role_getRoleListByGroup
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def getMenuPrivileges(self,version="v1"):
        """获取菜单权限"""
        # 请求参数
        params = {
            # 默认版本v1
            "_version":version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_shopweb_user_getMenuPrivileges
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def syscEnterpriseCode(self,orgId,enterpriseId,enterpriseCode,version="v1"):
        """同步企业代码"""
        # 请求参数
        params = {
            # 开放平台企业id
            "orgId" : str(orgId),
            # 业务平台企业id
            "enterpriseId" : str(enterpriseId),
            # 企业编码
            "enterpriseCode" : str(enterpriseCode),
            # 默认版本v1
            "_version":version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_gateway_syscEnterpriseCode
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result

    def getRoleAndUsersAsConfig(self,deptId,version="v1"):
        """获取对应角色列表对应的人员列表(请求头中必须有token参数，参数名为authenticator，该值从用户API中的登陆接口获得)"""
        # 请求参数
        params = {
            # 门店id
            "deptId" : str(deptId),
            # 默认版本v1
            "_version":version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_shopweb_role_getRoleAndUsersAsConfig
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result



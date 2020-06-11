import util.open_util
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
            "orgid":orgid,
            "_version":version,
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_gateway_authentication
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result



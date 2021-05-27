# 教程  
## 1. 项目启动类 ----> test_gateway.py  
    标记【TODO】的位置是需要填写和开发的  
## 2. 参考group文件夹中的api_gateway.py，进行开发  

```python
import group.gateway.gateway_const
import time
class ApiGateway():
    """权限API组"""
    def __init__(self,openPlateform):
        """构造方法"""
        self.open = openPlateform;

    def authentication(self,orgid,version="v1"):
        """TODO 接口名字： 根据组织机构代码获取开发者账号详细信息 ,网址： https://docs.open.ovopark.com/apidoc/detail/1/175/open.gateway.authentication/v2"""
        # 请求参数
        params = {
            #  ------------------- 业务参数 start ---------
            # 开放平台企业id
            "orgid":orgid,
            #  ------------------- 业务参数 end ---------
            # 默认版本v1 推荐版本v2
            "_version":version,
            # 时间戳
            "_timestamp": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            # 方法名指定 open.gateway.authentication
            "_mt":group.gateway.gateway_const.GatewayConst.method_open_gateway_authentication
        }
        self.open.createSign(params)
        result = self.open.httpRequest()
        # 发送请求
        return result
```
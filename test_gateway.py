import group.gateway.api_gateway
import util.base_client
import util.open_util
# 获取apiGateway对象

# 用户密匙 ，可以从账户中心查看
applicationkey ='S107-00000xxx'
# 用户密钥 ，可以从账户中心查看
applicationSecret ='xxxxxxxxxxxxxxxxxxxxxxxxx56756'
# 填写用户token，可以从用户登陆api获取
authenticator ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx331E433EE4FF4CF5AD600EDE2CA06B280AD2B5E2705387C46'
# 初始化用户的参数
openPlateform = util.base_client.BaseClient.initBaseClient(applicationkey,applicationSecret,authenticator)
# 初始化 根据组织机构代码获取开发者帐号详细信息 api
apiGateway = group.gateway.api_gateway.ApiGateway(openPlateform)
# 填写参数并发送请求
result = apiGateway.authentication(xxx,'v2')
print('最终的结果='+result)
print(apiGateway.getBusinessOrg(xxx))
print(apiGateway.getRoleListByGroup())
print(apiGateway.getMenuPrivileges())
print('同步企业代码='+apiGateway.syscEnterpriseCode(xxx,xxx,xxx))
print('获取对应角色列表对应的人员列表='+apiGateway.getRoleAndUsersAsConfig(xxxx))

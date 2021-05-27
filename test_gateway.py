import group.gateway.api_gateway
import util.base_client
import util.open_util
# 获取apiGateway对象

# TODO 用户密匙 ，可以从账户中心查看
applicationkey ='S107-00000xxx'
# TODO 用户密钥 ，可以从账户中心查看
applicationSecret ='xxxxxxxxx'
# TODO 填写用户token，可以从用户登陆api获取
authenticator ='0D1568C060D7E2FC0xxxxxxx139A3C9C552xxxxxxxx675365B'
# 初始化用户的参数
openPlateform = util.base_client.BaseClient.initBaseClient(applicationkey,applicationSecret,authenticator)




# (1) TODO 初始化 根据组织机构代码获取开发者帐号详细信息 api
apiGateway = group.gateway.api_gateway.ApiGateway(openPlateform)

# (2) TODO 填写参数并发送请求
print(apiGateway.authentication('xxxx','v2'));

# print(apiGateway.getBusinessOrg(269))
# print(apiGateway.getRoleListByGroup())
# print(apiGateway.getMenuPrivileges())
# print('同步企业代码='+apiGateway.syscEnterpriseCode(xxx,xxx,xxx))
# print('获取对应角色列表对应的人员列表='+apiGateway.getRoleAndUsersAsConfig(xxxx))

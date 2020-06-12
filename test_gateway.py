import group.gateway.api_gateway
import util.base_client
import util.open_util
# 获取apiGateway对象

# 用户密匙 ，可以从账户中心查看
applicationkey ='S107-00000183'
# 用户密钥 ，可以从账户中心查看
applicationSecret ='fa763b15729b35320270d326ee170bb8'
# 填写用户token，可以从用户登陆api获取
authenticator ='7E1AFAAA8D5E4C521C7ADD319F12BFE0D392E057CF5C659331E433EE4FF4CF5AD600EDE2CA06B280AD2B5E2705387C46'
# 初始化用户的参数
openPlateform = util.base_client.BaseClient.initBaseClient(applicationkey,applicationSecret,authenticator)
# 初始化 根据组织机构代码获取开发者帐号详细信息 api
apiGateway = group.gateway.api_gateway.ApiGateway(openPlateform)
# 填写参数并发送请求
result = apiGateway.authentication(262,'v2')
print('最终的结果='+result)
print(apiGateway.getBusinessOrg(262))
print(apiGateway.getRoleListByGroup())
print(apiGateway.getMenuPrivileges())
print('同步企业代码='+apiGateway.syscEnterpriseCode(262,262,262))
print('获取对应角色列表对应的人员列表='+apiGateway.getRoleAndUsersAsConfig(7192))
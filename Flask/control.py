# coding: utf-8
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.region.region import Region

ak = "AQXLDPRTOG1DBAFPUM2B"
sk = "8kcIhPlo3chnk14VHECa3sH98cx8CMY7SUYvP2Fi"

project_id = "4a339176169c42e885fe18af2e9e9a3d"
# region_id：如果是上海一，请填写"cn-east-3"；如果是北京四，请填写"cn-north-4"；如果是华南广州，请填写"cn-south-4"
region_id = "cn-north-4"
# endpoint：请在控制台的"总览"界面的"平台接入地址"中查看"应用侧"的https接入地址
endpoint = "f5f9b2a408.st1.iotda-app.cn-north-4.myhuaweicloud.com"


def openLight():
    # 标准版/企业版：需自行创建Region对象
    REGION = Region(region_id, endpoint)

    # 创建认证
    # 创建BasicCredentials实例并初始化
    credentials = BasicCredentials(ak, sk, project_id)

    # 标准版/企业版需要使用衍生算法，基础版请删除该配置
    credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

    # 基础版：请选择IoTDAClient中的Region对象 如： .with_region(IoTDARegion.CN_NORTH_4)
    # 标准版/企业版：需要使用自行创建的Region对象
    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(REGION) \
        .build()
    try:
        request = CreateCommandRequest()
        request.device_id = "649f8be69415fc7a573b373f_20230701"
        request.body = DeviceCommandRequest(
            paras="{\"Light\":\"ON\"}",
            command_name="Agriculture_Control_light",
            service_id="Agriculture"
        )
        response = client.create_command(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def closeLight():
    # 标准版/企业版：需自行创建Region对象
    REGION = Region(region_id, endpoint)

    # 创建认证
    # 创建BasicCredentials实例并初始化
    credentials = BasicCredentials(ak, sk, project_id)

    # 标准版/企业版需要使用衍生算法，基础版请删除该配置
    credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

    # 基础版：请选择IoTDAClient中的Region对象 如： .with_region(IoTDARegion.CN_NORTH_4)
    # 标准版/企业版：需要使用自行创建的Region对象
    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(REGION) \
        .build()
    try:
        request = CreateCommandRequest()
        request.device_id = "649f8be69415fc7a573b373f_20230701"
        request.body = DeviceCommandRequest(
            paras="{\"Light\":\"OFF\"}",
            command_name="Agriculture_Control_light",
            service_id="Agriculture"
        )
        response = client.create_command(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def closeMotor():
    # 标准版/企业版：需自行创建Region对象
    REGION = Region(region_id, endpoint)

    # 创建认证
    # 创建BasicCredentials实例并初始化
    credentials = BasicCredentials(ak, sk, project_id)

    # 标准版/企业版需要使用衍生算法，基础版请删除该配置
    credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

    # 基础版：请选择IoTDAClient中的Region对象 如： .with_region(IoTDARegion.CN_NORTH_4)
    # 标准版/企业版：需要使用自行创建的Region对象
    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(REGION) \
        .build()
    try:
        request = CreateCommandRequest()
        request.device_id = "649f8be69415fc7a573b373f_20230701"
        request.body = DeviceCommandRequest(
            paras="{\"Motor\":\"OFF\"}",
            command_name="Agriculture_Control_Motor",
            service_id="Agriculture"
        )
        response = client.create_command(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def openMotor():
    # 标准版/企业版：需自行创建Region对象
    REGION = Region(region_id, endpoint)

    # 创建认证
    # 创建BasicCredentials实例并初始化
    credentials = BasicCredentials(ak, sk, project_id)

    # 标准版/企业版需要使用衍生算法，基础版请删除该配置
    credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

    # 基础版：请选择IoTDAClient中的Region对象 如： .with_region(IoTDARegion.CN_NORTH_4)
    # 标准版/企业版：需要使用自行创建的Region对象
    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(REGION) \
        .build()
    try:
        request = CreateCommandRequest()
        request.device_id = "649f8be69415fc7a573b373f_20230701"
        request.body = DeviceCommandRequest(
            paras="{\"Motor\":\"ON\"}",
            command_name="Agriculture_Control_Motor",
            service_id="Agriculture"
        )
        response = client.create_command(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

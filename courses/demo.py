from kubernetes import client, config
import yaml
# from courses.kube_connect import create_service, create_deployment
from kubernetes.client.rest import ApiException


config.kube_config.load_kube_config(config_file="../kubeconfig.yaml")
api_instance = client.AppsV1Api()
# for service
CoreV1Api = client.CoreV1Api()


#
# # for service
coreApi = client.CoreV1Api()
#
# # for deployment
# appApi = client.AppsV1Api()
#
# # 命名空间
# for i in coreApi.list_namespace().items:
#     print(i.metadata.name)
#
# for i in coreApi.list_pod_for_all_namespaces().items:
#     print(i.metadata.name)

# te = coreApi.list_pod_for_all_namespaces()
# print(te)

#
# pods = coreApi.list_namespaced_pod(namespace = "default")
# print(pods)

# res = coreApi.read_namespaced_service(name='nginx-service', namespace='default')
# print(res)


# create_deployment(namespace=namespace, name=name, image_url=image_url)

# k8s_api_obj = client.AppsV1beta2Api()
# body = eval("{'kind': 'Deployment', "
#             "'spec': {'replicas': 1, 'template': {'spec': {'containers': [{'image': 'nginx:1.7.9', 'name': 'nginx', 'ports': [{'containerPort': 80}]}]}, 'metadata': {'labels': {'app': 'nginx-deployment'}}}, 'selector': {'matchLabels': {'app': 'nginx-deployment'}}}, 'apiVersion': 'apps/v1beta2', 'metadata': {'labels': {'app': 'nginx-deployment'}, 'namespace': 'default', 'name': 'nginx-deployment'}}")
#
# resp = k8s_api_obj.create_namespaced_deployment(body=body, namespace="default")
# print(resp)


# k8s_api_obj = client.CoreV1Api()
# namespace = "default"
# body = {'apiVersion': 'v1',
#         'kind': 'Service',
#         'metadata': {'name': 'nginx-service', 'labels': {'app': 'nginx'}},
#         'spec': {'ports': [{'port': 80, 'targetPort': 80}],
#                  'selector': {'app': 'nginx'},
#                  'type': 'LoadBalancer'
#                  }
#
#         }
#
# try:
#     api_response = k8s_api_obj.create_namespaced_service(namespace, body)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

# namespace = "default"
# body = {'apiVersion': 'apps/v1',
#         'kind': 'Deployment',
#         'metadata': {'name': 'nginx-deployment'},
#         'spec': {'replicas': 1,
#                  'selector': {'matchLabels': {'app': 'nginx'}},
#                  'template': {'metadata': {'labels': {'app': 'nginx'}},
#                               'spec': {
#                                   'containers': [{'name': 'nginx', 'image': 'nginx', 'ports': [{'containerPort': 80}]}]}
#                               }
#                  }
#
#         }
# resp = api_instance.create_namespaced_deployment(body=body, namespace="default")
# print(resp)

# res = api_instance.read_namespaced_deployment(name='nginx-deployment', namespace='default')
# print(res)

# namespace = "default"
# body = {'apiVersion': 'apps/v1',
#         'kind': 'Deployment',
#         'metadata': {'name': 'test03-deployment'},
#         'spec': {'replicas': 1,
#                  'selector': {'matchLabels': {'app': 'test03'}},
#                  'template': {'metadata': {'labels': {'app': 'test03'}},
#                               'spec': {
#                                   'containers': [{'name': 'test03',
#                                                   'image': 'yangxuan8282/alpine-xfce4-novnc:amd64',
#                                                   'ports': [{'containerPort': 6080}]}]}
#                               }
#                  }
#
#         }
# resp = api_instance.create_namespaced_deployment(body=body, namespace="default")
# print(resp)

res = CoreV1Api.read_namespaced_service(name='test03-nodeport-service', namespace='default')
print(res.spec.ports[0].node_port)

# k8s_api_obj = client.CoreV1Api()
# namespace = "default"
# body = {'apiVersion': 'v1',
#         'kind': 'Service',
#         'metadata': {'name': 'test02-service', 'labels': {'app': 'test02'}},
#         'spec': {'type': 'LoadBalancer',
#                  'ports': [{'port': 6080, 'targetPort': 6080}],
#                  'selector': {'app': 'test02'}}}
# try:
#     api_response = k8s_api_obj.create_namespaced_service(namespace, body)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)


# k8s_api_obj = client.CoreV1Api()
# namespace = "default"
# body = {'apiVersion': 'v1',
#         'kind': 'Service',
#         'metadata': {'name': 'test03-nodeport-service', 'labels': {'app': 'test03'}},
#         'spec': {'type': 'NodePort',
#                  'ports': [{'port': 6666, 'targetPort': 6080}],
#                  'selector': {'app': 'test03'}}}
# try:
#     api_response = k8s_api_obj.create_namespaced_service(namespace, body)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

# res = CoreV1Api.list_node().items[0]
# print(res.metadata.name)
# print(res.status.addresses[0].address)

import yaml
from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.kube_config.load_kube_config(config_file="../kubeconfig.yaml")

# for deployment
api_instance = client.AppsV1Api()

# for service
CoreV1Api = client.CoreV1Api()


def create_deployment(namespace, name, image_url):
    # deployment_info = api_instance.read_namespaced_deployment(namespace='default', name='')
    with open('../static/yaml/deployment.yaml') as f:
        body = yaml.safe_load(f)

    body['metadata']['name'] = name + "-deployment"
    body['metadata']['namespace'] = namespace
    body['spec']['selector']['matchLabels']['app'] = name
    # body.spec.selector.matchlabels.app = name
    body['spec']['template']['metadata']['labels']['app'] = name
    # body.spec.template.metadata.labels.app = name
    body['spec']['template']['spec']['containers'][0][name] = name
    # body.spec.template.spec.containers[0].name = name
    body['spec']['template']['spec']['containers'][0]['image'] = image_url
    # body.spec.template.spec.containers[0].image = image_url
    api_instance.create_namespaced_deployment(namespace=namespace, body=body)


def delete_deployment(namespace, name):
    api_instance.delete_namespaced_deployment(namespace=namespace, name=name)


def create_service(namespace, name, container_port, type='NodePort'):
    with open('../static/yaml/service.yaml', mode='r', encoding='UTF-8') as f:
        body = yaml.safe_load(f)

    body['metadata']['name'] = name + "-service"
    body['metadata']['namespace'] = namespace
    body['metadata']['labels']['app'] = name
    body['spec']['type'] = type
    body['spec']['ports'][0]['targetPort'] = container_port
    body['spec']['selector']['app'] = name

    CoreV1Api.create_namespaced_service(namespace=namespace, body=body)


def delete_service(namespace, name):
    CoreV1Api.delete_namespaced_service(namespace=namespace, name=name)


def read_service_info(name, namespace='default'):
    service_info = CoreV1Api.read_namespaced_service(name=name,namespace=namespace)

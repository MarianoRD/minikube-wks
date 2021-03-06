# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Source: https://github.com/kubernetes-client/python/blob/master/examples/example1.py
from kubernetes import client, config
import os


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    # Change kube config location (set up in scripts/env-minikube.sh)
    kubeconfig = os.environ['KUBECONFIG']

    config.load_kube_config(config_file=kubeconfig)

    v1 = client.CoreV1Api()
    print("\nListing pods with their IPs:\n\n")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    print("{:15s} {:30s} {:50s}".format("Pod IP", "Namespace", "Pod Name"))
    print("-"*100)
    for i in ret.items:
        print("{!s:15s} {:30s} {:50s}".format(i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
  main()
# Kubernetes

# Requirements

* Minikube
* Editor

# What is kubernetes

* Container Orchestration Software
* Started out at Google, now used and developed by Amazon, Microsof, Google, RedHat...

# Parts

* etcd - Key-Value-Store
* kube-apiserver - API
* kube-scheduler - Chooses Nodes for Pods (ressources, limits, constraints, ...)
* kube-controller-managers - Controller (manage resources)

# Minikube

* `minikube start --vm-driver kvm2`
* `minikube addons enable registry`
* ```
  pod=$(kc get pods -n kube-system -o json | jq -r '.items | .[] | select(.metadata.ownerReferences | first | .name == "registry") | "pod/\(.metadata.name)"')
  kc port-forward "$pod" -n kube-system 5000:5000
  ```

# Live Demo

```
kc apply -f 00-namespace.yml 
. environment
envsubst < secret.yml.envsubst  | kc apply -f -
kc apply -f .
```

# Things to look into

* HELM - Template Deployments
* kubectl kustomize - Overwrites
* kube-score - Linter
* CRDs - Custom Resource Definitions

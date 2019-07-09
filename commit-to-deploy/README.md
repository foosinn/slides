# Commit to Deploy

* setup
  ```sh
  # start minikube
  minikube start --vm-driver kvm2 --insecure-registry 10.0.0.0/24
  minikube addons enable ingress

  # you need to replace the service ip
  minikube ip
  find -type f -print0 | xargs -0 sed 's/192.168.39.37/192.168.39.37/g' -i

  # apply manifests
  kc apply -f manifests/
  kc get pods -w

  # hack to make in cluster registry reachable
  minikube ssh -- bash -c "whoami; echo $(kc get service registry -o jsonpath="{.spec.clusterIP}") registry.default.svc \
    | sudo tee /etc/hosts"

  # get urls
  kc get ingress
  ```

* setup tiller
```
helm init --tiller-namespace=myapp --upgrade
helm init --tiller-namespace=myapp-staging --upgrade
```

* create git user
* create git repo
* add secrets to drone
  ```
  kc get secrets --all-namespaces -o json \
    | jq -r '.items|.[]|select(.metadata.name|test("default-token.*"))|select(.metadata.namespace|test("myapp.*")) |"\(.metadata.namespace) \(.data.token|@base64d)"'
  ```

* add repo in drone
* put myapp in gitrepo

# Kubernetes Volumes

## emptyDir
An `emptyDir` volume is first created when a Pod is assigned to a Node, and exists as long as that Pod is running on that node. It's initially empty.
Example:
```yaml
volumes:
- name: cache-volume
  emptyDir: {}
```

## hostPath
A `hostPath` volume mounts a file or directory from the host node's filesystem into your Pod. Useful for things like node-level logging.
Example:
```yaml
volumes:
- name: node-log
  hostPath:
    path: /var/log
```

## PersistentVolume (PV)
A piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes. It has a lifecycle independent of any individual Pod.

## PersistentVolumeClaim (PVC)
A request for storage by a user. Claims can request specific size and access modes.

## StorageClass
Provides a way for administrators to describe the "classes" of storage they offer. Different classes might map to quality-of-service levels, or to backup policies.

## Dynamic Provisioning
When none of the static PVs the administrator created match a user's PVC, the cluster may try to dynamically provision a volume for the PVC, based on the StorageClass.

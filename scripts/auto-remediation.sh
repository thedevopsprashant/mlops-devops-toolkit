#!/bin/bash

NAMESPACE=production

echo "Checking unhealthy pods..."

pods=$(kubectl get pods -n $NAMESPACE | grep CrashLoopBackOff | awk '{print $1}')

for pod in $pods
do
    echo "Restarting pod: $pod"
    kubectl delete pod $pod -n $NAMESPACE
done

echo "Auto-remediation completed."

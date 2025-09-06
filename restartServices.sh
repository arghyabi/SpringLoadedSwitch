#!/bin/bash

SERVICES=("spring-loaded-switch-php.service" "spring-loaded-switch-python.service")

echo "Checking status before restart..."
for SERVICE in "${SERVICES[@]}"; do
    echo "Status of $SERVICE:"
    sudo systemctl status "$SERVICE" --no-pager
    echo "-----------------------------"
done

echo "Restarting services..."
for SERVICE in "${SERVICES[@]}"; do
    if ! sudo systemctl restart "$SERVICE"; then
        echo "ERROR: Failed to restart $SERVICE" >&2
    fi
done

echo "Checking status after restart..."
for SERVICE in "${SERVICES[@]}"; do
    echo "Status of $SERVICE:"
    sudo systemctl status "$SERVICE" --no-pager
    echo "-----------------------------"
done

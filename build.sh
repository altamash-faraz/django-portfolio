#!/usr/bin/env bash
# build.sh
set -o errexit

echo "Installing Python packages..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "Running database migrations..."
python manage.py migrate

echo "Build completed successfully!"
#!/bin/bash

if [[ $VERCEL_ENV == "production" ]]; then
  echo "Running migrations in production..."
  python manage.py migrate
else
  echo "Running migrations in preview..."
  python manage.py migrate
fi

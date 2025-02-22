#!/bin/bash
celery -A data_archival worker --loglevel=info &  # Run worker in the background
celery -A data_archival beat --loglevel=INFO       # Run beat in the foreground
wait  # Wait for any background processes to finish

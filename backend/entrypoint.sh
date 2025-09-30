#!/bin/sh
# This script is the official entrypoint for the Docker container.
# It runs the Uvicorn server using its absolute path to be 100% sure.

/root/.local/bin/uvicorn src.main:app --host 0.0.0.0 --port 10000
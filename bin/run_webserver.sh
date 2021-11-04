#!/bin/bash
./bin/migrate.sh
python -m providers.web.fastapi.main

docker-compose run --rm app ./bin/migrate.sh
docker-compose run --rm app python3 -m unittest discover -s "/opt/app/tests"

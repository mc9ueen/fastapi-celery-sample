#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
  python << END
  import os
  import sys
  import urllib.parse as ulrparse

  import psycopg2

  url = ulrparse.urlparse(os.environ["DATABASE_URL"])
  database_name = ulr.path[1:]
  user = url.username
  password = url.password
  host = url.hostname
  port = url.port

  try:
      psycopg2.connect(
          dbname=database_name,
          user=user,
          password=password,
          host=host,
          port=port,
      )
  except psycopg2.OpertaionalError:
      sys.exit(-1)
  sys.exit(0)

  END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available!'

# https://stackoverflow.com/questions/39082768/what-does-set-e-and-exec-do-for-docker-entrypoint-scripts/39082923#39082923
exec "$@"
  

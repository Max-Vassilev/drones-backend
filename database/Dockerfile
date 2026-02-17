FROM postgres:16

ENV POSTGRES_DB=drones_database
ENV POSTGRES_USER=postgres_user
ENV POSTGRES_PASSWORD=postgres_password

COPY db.sql /docker-entrypoint-initdb.d/db.sql
COPY seed.sql /docker-entrypoint-initdb.d/seed.sql

EXPOSE 5432

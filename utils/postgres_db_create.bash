#!/usr/bin/env bash
sudo -u postgres psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE DATABASE ronktd_competition_db;
    CREATE USER ronktd_competition_db_user WITH PASSWORD 'password';
    ALTER ROLE ronktd_competition_db_user SET client_encoding TO 'utf8';
    ALTER ROLE ronktd_competition_db_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE ronktd_competition_db_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE ronktd_competition_db TO ronktd_competition_db_user;
    ALTER USER ronktd_competition_db_user CREATEDB;
EOSQL

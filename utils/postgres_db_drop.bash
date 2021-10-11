#!/usr/bin/env bash
sudo -u postgres psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    DROP DATABASE IF EXISTS ronktd_competition_db;
    DROP DATABASE IF EXISTS test_ronktd_competition_db;
    DROP USER IF EXISTS ronktd_competition_db_user;
    DROP USER IF EXISTS test_ronktd_competition_db_user;
EOSQL

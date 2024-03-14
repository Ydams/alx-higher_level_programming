#!/bin/bash

# MySQL credentials
MYSQL_USER="mysql_user"
MYSQL_PASSWORD="mysql_password"

# MySQL command to get privileges
MYSQL_COMMAND="mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e"

# Query to list privileges of user_0d_1
QUERY_USER_0D_1="SELECT * FROM information_schema.user_privileges WHERE GRANTEE='''user_0d_1'@'localhost''';"

# Query to list privileges of user_0d_2
QUERY_USER_0D_2="SELECT * FROM information_schema.user_privileges WHERE GRANTEE='''user_0d_2'@'localhost''';"

# Execute the queries
echo "Privileges for user_0d_1:"
$MYSQL_COMMAND "$QUERY_USER_0D_1"

echo "Privileges for user_0d_2:"
$MYSQL_COMMAND "$QUERY_USER_0D_2"


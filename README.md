# Composer-to-execute-sql-query
Scheduling to execute the Cloud postgresql queries from Composer

### Considering that already you have created the postgresql instance in your google cloud sql-query

### Then set the connection variable from airflow composer as following steps

Admin-->connection-->create

conn id:  <connection id name>  e.g. Postgresql_mart_conn

Conn Type : select "Google cloud SQL" from drop down

Host  : <public id add> e.g. 34.101.143.68

Schema :<DB name>  e.g. mart

Login  :<login user> e.g. postgres

Password  : <password to connect db>

Extra  : <provide the below details>  

e.g.  {

   "database_type": "postgres",
   
   "project_id": "third-campus-303308",
   
   "location": "europe-west2",
   
   "instance": "postgresql-1",
   
   "use_proxy": true,
   
   "sql_proxy_use_tcp": false
   
}


### Place the cloud_psql_query_dag.py file into the dag folder.

The dag folder is created in the cloud storage during Composer instance creation.

### Click on the Airflow link i.e. under 'Airflow webserver' tab of the Composer instance.

### You will find a new dag instance(execute-cloud-psql-query) for the new file placed in the cloud storage dag folder.

### Monitor the dag which will be executed at every 5 minutes.

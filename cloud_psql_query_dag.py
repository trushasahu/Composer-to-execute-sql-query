##Using Composer to schedule sql queries

from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
#from airflow.operators import  PostgresOperator
#from airflow.providers.google.cloud.operators.cloud_sql import CloudSQLExecuteQueryOperator
from airflow.contrib.operators.gcp_sql_operator import CloudSqlQueryOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 6, 30),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(dag_id='execute-cloud-psql-query', catchup=False, default_args=default_args, schedule_interval='*/5 * * * *') #exeute at every 5 minutes

#t1 = PostgresOperator(
#    task_id='psql_insert',
#    postgres_conn_id='Postgresql_mart_conn',
#    provide_context=True,
#    sql=""" insert into data_load.item_details select item_identifier  ,item_weight,item_fat_content from data_load.bigmart_data; """,
#    dag=dag)
	
t1 = CloudSqlQueryOperator(
    task_id='psql_insert',
    gcp_cloudsql_conn_id='Postgresql_mart_conn',
    provide_context=True,
    sql=""" insert into data_load.item_details select item_identifier  ,item_weight,item_fat_content from data_load.bigmart_data limit 5; """,
    dag=dag)	


t1

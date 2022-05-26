from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import dates_ago

##dag arguements
default_arguements={
    'owner': 'NilakanthaSDeo',
    'start_date': days_ago(0),
    'email': ['nilakantha.deo@kpipartners.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),    
}
# define the DAG
dag = DAG(
    'my-first-dag',
    default_args=default_args,
    description='default_arguements',
    schedule_interval=timedelta(days=1),
)
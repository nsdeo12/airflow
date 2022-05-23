from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago 

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
##dag definition
dag = DAG(
    dag_id='sample-etl-dag',
    default_args=default_arguements,
    description='Sample ETL DAG using Bash',
    schedule_interval=timedelta(days=1),
)
##task definition
extract = BashOperator(
    task_id='extract',
    bash_command='echo "extract"',
    dag=dag,
)


# define the second task named transform
transform = BashOperator(
    task_id='transform',
    bash_command='echo "transform"',
    dag=dag,
)

# define the third task named load

load = BashOperator(
    task_id='load',
    bash_command='echo "load"',
    dag=dag,
)

##task pipeline
extract>>transform>>load
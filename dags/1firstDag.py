# python library imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt
#########################################
########### DAG arguements ##############
#########################################
default_args={
 'owner':'me',
 'start_date':dt.datetime(2022,5,20),
 'retries':1,
 'retry_delay':dt.timedelta(minutes=5)
}
#########################################
######## DAG definitions ################
#########################################
dag=DAG('simple_example',
        description='A simple dag',
        default_args=default_args,
        schedule_interval=dt.timedelta(seconds=5)
        )
#########################################
######### Task definitions ##############
#########################################
task1= BashOperator(
    task_id="print_hello",
    bash_command='echo "Hi from bash operator"',
    dag=dag
)
task2 = BashOperator(
    task_id="print_date",
    bash_command='date',
    dag=dag
)
#########################################
############## Task pipeline ############
#########################################
task1>>task2
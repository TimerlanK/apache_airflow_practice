from airflow import DAG
from airflow.operators.python import PythonOperator
from hooks.elastic.elastic_hook import ElasticHook
 
from datetime import datetime
 
def _print_es_info():
    hook = ElasticHook()
    info = hook.info()  # Call the info method and store the result in a variable
    print(info)  # Print the information retrieved from the Elasticsearch cluster


with DAG('elastic_dag', start_date=datetime(2022, 1, 1), schedule_interval='@daily', catchup=False) as dag:
 
    print_es_info = PythonOperator(
        task_id='print_es_info',
        python_callable=_print_es_info
    )
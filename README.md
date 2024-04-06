This project is designed to provide hands-on experience with various aspects of Data Engineering, focusing on the practical application of different operators, scheduling methods and some advanced concepts.

Core Components and Examples:
- **Branching with branch_operator_dag**
  </br>Implement branching operators to control the flow of execution based on specific conditions.
  </br>**dags/branch_operator.py**
  </br>![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/262adf75-afdd-4212-9ce6-5b954018f51b)

  ---

- **Dataset Scheduling with consumer and producer DAGs**
  </br>Utilize the dataset method for new scheduling techniques to handle dependencies and trigger tasks in a data-driven approach.
  </br>**dags/producer.py and dags/consumer.py**
  </br>![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/6e8d6e01-1b89-4247-a467-72a92aa55983)

  ---

- **Grouping and Task Management with group_dag and task_dag**
  </br>Practice grouping tasks as subDAGs and using task groups for better organization and parallel execution within workflows.
  </br>**dags/group_dag.py, dags/subdags/subdag_downloads.py and dags/subdags/subdag_transforms.py**
  </br>![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/de4a7e72-5a48-4350-a1f3-33cf77d92b8a)![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/b54b44f9-9015-42f4-b5ed-f32fec8ecec1)![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/53c67283-6d81-4222-9eff-28a229c20196)
  </br>**dags/task_dag.py, dags/groups/group_downloads.py and dags/groups/group_transforms.py**
  </br>![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/f8ad964f-655f-4084-b947-374cd430123c)

  ---
  
- **Custom Plugins with elastic_dag**
  </br>Develop custom plugins and integrate with Elasticsearch for dynamic data querying and indexing.
  </br> **elastic_dag.py and plugins/hooks/elastic**
  </br>![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/30eebda8-b9ff-4921-803a-c491baccdd16)

  ---
  
- **Cross-Communication with xcom_dag**
  </br>Explore cross-communication between tasks using XCom to pass and share results.
  </br> **dags/xcom_dag.py**
  </br> ![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/e6931ac4-f8e8-4008-b407-74c43102faba)

  ---
  
- **Parallel Execution with parallel_dag**
 </br>Test the parallel processing capabilities of tasks across different nodes using a Celery worker for efficient workload management.
 </br> **dags/parallel_dag.py**
 </br> ![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/e3447931-9c91-44fb-b0a6-07266b2e8a68)![image](https://github.com/TimerlanK/apache_airflow_practice/assets/59342509/7a0f313a-0a48-4c37-8ed7-e58905d5e426)
 </br> 4 tasks are in default worker and transform task is in high_cpu worker

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator", # airflow 웹 사이트에 뜨는 DAG 이름, 주로 파일 이름과 동일하게 만듦
    schedule="30 6 * * *", # (주기적으로) 언제 도는지 -> (분, 시, 일, 월, 요일)
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"), # 언제부터 시작하는지
    catchup=False, # 현재 시점과 start_date 차이에 대한 소급 적용 여부
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0, 3)
        print(fruit[rand_int])
        
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )
    
    py_t1

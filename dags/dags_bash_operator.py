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
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # airflow 웹 사이트에 뜨는 DAG 이름, 주로 파일 이름과 동일하게 만듦
    schedule="0 0 * * *", # (주기적으로) 언제 도는지 -> (분, 시, 일, 월, 요일)
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"), # 언제부터 시작하는지
    catchup=False, # 현재 시점과 start_date 차이에 대한 소급 적용 여부
    dagrun_timeout=datetime.timedelta(minutes=60), # timeout 되는 시간
    tags=["example", "example2"], # airflow 웹 사이트에 뜨는 tagging, 공통적으로 보는 것을 확인할 수 있음
    params={"example_key": "example_value"}, # DAG 단위의 공통 input parameter
) as dag:
    run_this_last = EmptyOperator(
        task_id="run_this_last",
    )

    # [START howto_operator_bash]
    
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    ) # Operator를 통해 instance화 -> Task
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    ) # Operator를 통해 instance화 -> Task

    # task 간의 선행 관계, t1 이후에 t2 수행하도록 함
    bash_t1 >> bash_t2
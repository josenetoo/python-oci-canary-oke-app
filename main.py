from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/canary")
def read_root():
    version="2.0"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "Oracle DevOps Day - OCI Devops!!!","Version":version,"Namespace":namespace}

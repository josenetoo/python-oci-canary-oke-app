# from typing import Optional

# from fastapi import FastAPI

# import os

# app = FastAPI()


# @app.get("/canary")
# def read_root():
#     version="1.0"
#     namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
#     return {"Message": "Oracle DevOps Day - OCI Devops!! Casa Oracle!!","Version":version,"Namespace":namespace}

from typing import Dict
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/canary")
def read_root() -> Dict[str, str]:
    """
    OCI DevOps
    """
    version = "2.0"
    namespace = os.getenv('POD_NAMESPACE', default='ns-red')
    return {
        "Message": "Oracle DevOps Day - OCI DevOps!! Casa Oracle!!",
        "Version": version,
        "Namespace": namespace,
        "Logo": "https://www.oracle.com/favicon.ico"  # Link to Oracle Cloud logo
    }

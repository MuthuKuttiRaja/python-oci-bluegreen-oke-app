from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    version="0.2"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "with More Love from OCI Devops ","Version":version,"Namespace":namespace}

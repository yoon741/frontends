from pydantic import BaseModel

class Emp(BaseModel):
    empid: int
    fname: str
    lname: str
    email: str
    phone: str
    hdate: str
    jobid: str
    sal: int
    comm: float
    mgrid: int
    deptid: int
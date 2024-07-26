from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.schema.emp import Emp

# 라우터 생성
emp_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정
@emp_router.get('/', response_class=HTMLResponse)
async def emp(req: Request):
    return templates.TemplateResponse('emp/emp.html',{'request': req})

@emp_router.post('/', response_class=HTMLResponse)
async def empok(req: Request,
                empid = Form(...), fname= Form(...), lname=Form(...),
                email=Form(...), phone=Form(...), hdate=Form(...),
                jobid=Form(...), sal=Form(...), comm=Form(...),
                mgrid=Form(...), deptid=Form(...)):
                # empid: int = Form(...), fname: str = Form(...), lname: str = Form(...),
                # email: str = Form(...), phone: str = Form(...), hdate: str = Form(...),
                # jobid: str = Form(...), sal: int = Form(...), comm: float = Form(...),
                # mgrid: int = Form(...), deptid: int = Form(...)):
                
    emp = Emp(empid=empid, fname=fname, lname=lname, email=email,
                   phone=phone, hdate=hdate, jobid=jobid, sal=sal,
                   comm=comm, mgrid=mgrid, deptid=deptid)
    return templates.TemplateResponse('emp/result.html',
                                      {'emp': emp, 'request': req})
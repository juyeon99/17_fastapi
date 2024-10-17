from fastapi import FastAPI

app = FastAPI()

# 쿼리 파라미터
# url 뒤에 ? key-value 쌍으로 들어가는 파라미터
@app.get("/teachers/")
async def print_teacher_num(
    num: int, 
    name: str = "default"   # name 기본 값 default
):
    return {f"num:{num}, name:{name}"}

# 쿼리 매개변수를 필수로 만드려면 가본값을 설정하지 않으면 된다.
# 다양한 매개변수를 작성할 때 매개변수는 이름으로 찾아지기 때문에 순서는 상관 X

# 선택적 매개변수
from typing import Union

@app.get("/teacher/{teacher_id}")
async def print_teacher(
    teacher_id: int,                # path parameter
    name: Union[str, None] = None   # query parameter / Optional
):
    # name 값이 있으면 id, name 둘 다 응답
    if name:
        return {f"teacher_id:{teacher_id}, teacher_name:{name}"}
    return {f"teacher_id:{teacher_id}"}
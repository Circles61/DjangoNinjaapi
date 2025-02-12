# DjangoNinjaAPI/trunk/study_router.py
#路由创建方式二：模块化管理路由
#将新增接口放在独立的 Router 文件中，或者独立的py文件中
#例如：
'''
# DjangoNinjaAPI/trunk/study_router.py
from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from trunk.models import StudyData  # 假设有 StudyData 模型
from trunk.serializers import StudyDataSchema  # 定义在 serializers.py 中

study_router = Router()

@study_router.get("/", response=list[StudyDataSchema])
def list_study_data(request):
    return StudyData.objects.all()

@study_router.get("/{study_id}", response=StudyDataSchema)
def get_study_data(request, study_id: int):
    return get_object_or_404(StudyData, id=study_id)

@study_router.post("/", response={201: dict})
def create_study_data(request, data: StudyDataSchema):
    new_data = StudyData.objects.create(**data.dict())
    return {"message": "创建成功", "study_id": new_data.id}

@study_router.put("/{study_id}", response={200: dict})
def update_study_data(request, study_id: int, data: StudyDataSchema):
    study_obj = get_object_or_404(StudyData, id=study_id)
    for key, value in data.dict().items():
        setattr(study_obj, key, value)
    study_obj.save()
    return {"message": "更新成功"}

@study_router.delete("/{study_id}", response={200: dict})
def delete_study_data(request, study_id: int):
    study_obj = get_object_or_404(StudyData, id=study_id)
    study_obj.delete()
    return {"message": "删除成功"}

'''
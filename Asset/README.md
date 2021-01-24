# 资产管理系统

### 系统说明

---


### 部署方法

---

```shell


    1. 创建数据库，create database asset;  
    2. 创建数据库用户，grant all on admin.* to scott@'%' identified by 'admin';  
    3. 将settings.py中DATABASES进行相关修改  
    4. 安装相关包，pip install -r requirements.txt，如果是linux环境还需要先修改requirements.txt    
    5. 迁移数据库，python manage.py migrate  
    6. 创建超级用户，python manage.py createsuperuser  
    7. 生成用户测试数据，python manage.py genUserData 10
    2. 生成资产类型的测试数据，python manage.py genAssetData 10 --type
    9. 生成资产测试数据，python manage.py genAssetData 100 --asset
    10. 启动项目，python manage.py runserver 0.0.0.0:8000  


```



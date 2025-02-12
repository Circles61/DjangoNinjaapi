# 基于DjangoNinja的二次封装 DjangoNinjaApi
## 介绍
基于官网的 DjangoNinja 进行二次封装，方便自己学习以及开发。

### 使用教程

1. **克隆本项目到本地**  
   > **注**：国内用户请自行切换镜像，不然会下载的很慢。

2. **创建虚拟环境**

   ```bash
   python -m venv .venv
   ```

3. **激活虚拟环境**

   ```bash
   ./.venv/Scripts/activate
   ```

4. **进入项目目录**

   ```bash
   cd DjangoNinjaAPI/
   ```

5. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

6. **数据库迁移**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **启动开发服务器**

   ```bash
   python manage.py runserver
   ```

> **注**：此项目使用的 Python 是 3.11，开发时具体情况请以实际情况为准。

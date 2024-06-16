# 使用官方的 Python 镜像
FROM python:3.9.7

# 设置工作目录
WORKDIR /usr/app

# 复制应用程序代码到容器中
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 安装 PostgreSQL 客户端和服务端
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# 切换到 postgres 用户并启动 PostgreSQL server, 创建数据库和加载 schema
USER postgres
RUN service postgresql start && \
    sleep 5 && \
    createdb webchatting && \
    psql -d webchatting -f /usr/app/schema.sql

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV SECRET_KEY=95d3763bb55e744e77dd181a47b4e1c6
ENV DATABASE_URL=postgresql:///webchatting

# 暴露端口
EXPOSE 5000

# 使用 entrypoint 脚本启动
CMD service postgresql start && flask run --host=0.0.0.0 --port=5000


#docker build . -t webchatting 
#docker run -it -p 5001:5000 webchatting
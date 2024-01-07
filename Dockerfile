FROM python:3.8-slim-bullseye

# 设置时间为上海时间
ENV TZ=Asia/Shanghai DEBIAN_FRONTEND=noninteractive

RUN sed -i s/deb.debian.org/mirrors.ustc.edu.cn/g /etc/apt/sources.list

RUN apt update \
    && apt install -y tzdata \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple

COPY ./ /app/

CMD python -m server.main
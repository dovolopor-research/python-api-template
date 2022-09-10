# Python API Template

🐍 一个**快速高性能**的「Python API 模板」

## 1 目录简介

```
.
├── README.md             # 简介
├── server                # 部署
│   └── app.py
├── conf                  # 配置
│   ├── default.prod.yml
│   ├── default.test.yml
│   └── default.yml
├── util                  # 辅助
│   ├── arg.py
│   ├── conf.py
│   ├── log.py
│   ├── data_model.py
│   └── db.py
├── test                  # 测试（可选）
│   └── api_test.py
├── doc                   # 文档（可选）
├── log                   # 日志
├── Dockerfile            # Docker 打包配置（可选）
├── .dockerignore         # Docker 忽略配置（可选）
├── .gitignore            # Git 忽略配置
├── requirements.txt      # 依赖（可选）
└── LICENSE               # 许可
```

### 1.1 README.md（文档）

**一个详尽的文档比什么都重要！** 任何人都可以通过文档快速上手。也许你会说，我的代码就我自己看，不写文档也知道。可是你能保证三个月以后，你还记得你当初写的什么吗？！

一个好的深度学习项目文档应该是怎样的？

1. 环境依赖说明
2. 快速运行脚本
3. 类似项目比较
4. 性能测试结果
5. 细致版本记录
6. 相关参考资料

参考：

1. [如何写好Github中的readme？](https://www.zhihu.com/question/29100816)
2. [如何为你的开源项目编写实用的文档](https://zhuanlan.zhihu.com/p/120399648)

### 1.2 util（辅助工具）

一些常见的辅助函数，比如：

1. conf 配置
2. arg 参数
3. data_model 数据模型
4. log 日志
5. db 数据库

### 1.3 conf（配置中心）

所有的配置都是用 `YAML`，它比 `json` 更好用，可以在配置中添加注释，并且呈现方式也更为直观！

配置文件的中间名称是「环境变量」，比如 ENV 为 `test` 时，就会读取 `default.test.yml` 文件（ENV 默认为 `dev`，会读取 `default.yml`）。

如何使用环境变量 ENV 呢？只需要在执行时，把 `-e test` 添加到命令的后面。

```shell
python -m server.main -e test
# or
python -m server.main --env test
```

### 1.4 server（部署）

使用 Web 服务部署到线上环境，推荐使用 [Sanic](https://sanic.dev/zh/)。

```shell
python -m server.main
```

### 1.5 test（测试）

`api_test.py` 是对 API 接口进行压力测试，得到 QPS（每秒请求数）。

`Locust` 是一个非常好用的测试工具，它附带一个 WEB 界面，非常方便地在浏览器中进行压测。

```shell
locust -f test/api_test.py -u 10 -r 1
```

在浏览器中打开 `http://127.0.0.1:8089`，点击 `Start swarming` 按钮，就可以开始压测了！

参考：
1. [Python unittest: 单元测试框架](https://docs.python.org/zh-cn/3/library/unittest.html)
2. [Locust: An open source load testing tool.](https://locust.io)

### 1.6 doc（文档｜可选）

如果项目比较复杂，可以将文档整理归纳到这里。

### 1.7 log（日志）

`util/log.py` 会将日志按天记录到这里。

### 1.8 requirements.txt （依赖）

项目所需要的依赖，方便一键安装。

```shell
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

参考：

1. [有关 pip 的使用](https://www.v2ai.cn/2019/12/20/python/7-pip/)

### 1.9 LICENSE（许可｜可选）

如果是开源项目，需要添加许可证。

参考：

1. [一文看懂开源许可证丨开源知识科普](https://pingcap.com/zh/blog/introduction-of-open-source-license)
2. [如何选择开源许可证？](https://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html)

## 2 环境准备

- Ubuntu 18.04 LTS+
- Python 3.7+
- Anaconda 3

> 人生苦短，快用 `*NIX` ！

## 3 容器化部署

```shell
cd python-api-template
# 打包
docker build -t python-api:0.1.0 .

# 运行
docker run -d --name python-api -p 9999:9999 \
  -v $PWD/conf/default.test.yaml:/app/conf/default.yaml \
  python-api:0.1.0

# 查看
docker logs -f python-api

# 调用 API
curl --location --request POST 'http://127.0.0.1:9999/test' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test"
}'
```

## 4 参考

- [Ubuntu 系统镜像下载](https://cn.ubuntu.com/download)
- [Anaconda 个人版](https://www.anaconda.com/products/individual#)
- [TUNA 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)

## 5 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

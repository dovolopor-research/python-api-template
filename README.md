# Python API Template

🐍 一个**快速高性能**的「Python API 模板」

## 0 快速启动

```shell
pip install -r requirements.txt

python -m server.main
```

## 1 目录简介

```
.
├── README.md             # 简介
├── server                # 部署
│   └── app.py
├── conf                  # 配置
│   ├── default.prod.yaml # 生产配置
│   ├── default.test.yaml # 测试配置
│   └── default.yaml      # 开发配置
├── util                  # 辅助
│   ├── conf.py
│   ├── log.py
│   └── data_model.py     # 类型定义
├── script                # 脚本
│   ├── sync.sh           # 同步到服务器
│   ├── build.sh          # 打包镜像
│   └── run.sh            # 运行容器
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

一个好的项目文档应该是怎样的？

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
2. data_model 类型注解
3. log 日志

### 1.3 conf（配置中心）

所有的配置都是用 `YAML`，它比 `json` 更好用，可以在配置中添加注释，并且呈现方式也更为直观！

配置文件的中间名称是「环境变量」，比如 ENV 为 `test` 时，就会读取 `default.test.yaml` 文件（ENV 默认为 `dev`，会读取 `default.yaml`）。

如何使用环境变量 ENV 呢？只需要在执行时，把 `ENV=test` 添加到命令的最前面，比如 `ENV=test python -m server.main`。

```shell
# 默认是 ENV 是 dev
python -m server.main
# or
ENV=dev python -m server.main
```

### 1.4 server（部署）

使用 Web 服务部署到线上环境，推荐使用 [FastAPI](https://fastapi.tiangolo.com/zh/)。

1. **高性能**：FastAPI 是基于 Starlette 和 Pydantic 构建的，因此它具有非常高的性能。与其他 Python Web 框架相比，它的速度更快，甚至可以与 Node.js 和 Go 这样的高性能语言竞争。
2. **易用性和开发效率**：FastAPI 使用了现代 Python 特性，如类型提示，使得代码易于阅读和编写。这有助于提高开发者的生产力以及减少错误。另外，它自动生成 API 文档（使用 OpenAPI 和 JSON Schema），方便开发者查看和测试 API 接口。
3. **丰富地插件和社区支持**：FastAPI 提供了许多内置组件，如身份验证、安全、数据验证等，可帮助您快速构建 Web 应用。同时，由于 FastAPI 的普及，其拥有一个庞大的活跃社区，为开发者提供大量第三方库和技术支持。

> 在过去本项目推荐使用 [Sanic](https://sanic.dev/zh/)，你可以在这个分支 [branch/sanic](https://github.com/Ailln/python-api-template/tree/sanic) 找到过去的代码。

```shell
# 开发环境运行
python -m server.main

# 测试环境运行
ENV=test python -m server.main

# 生产环境运行
ENV=prod python -m server.main
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

`util/log.py` 会将日志按天记录到 log 目录下。

### 1.8 requirements.txt （依赖）

项目所需要的依赖，方便一键安装。

```shell
# 直接安装
pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
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
- Python 3.8+
- Docker 21+

> 人生苦短，快用 `*NIX` ！

## 3 容器化部署

```shell
cd python-api-template

# 直接打包
docker build -t python-api-template:1.0.0 .
# or 使用脚本打包
bash script/build.sh

# 直接运行
docker run -d  --restart=always \
  --name python-api \
  -p 9999:9999 \
  -v $PWD/conf/:/app/conf \
  -e ENV=prod \
  python-api-template:1.0.0
# or 使用脚本运行
bash script/run.sh

# 查看
docker logs -f python-api-template

# 调用 API
curl --location --request POST 'http://127.0.0.1:9999/test' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data": "test"
}'
```

## 4 参考

- [Ubuntu 系统镜像下载](https://cn.ubuntu.com/download)
- [Anaconda 个人版](https://www.anaconda.com/products/individual#)
- [TUNA 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)

## 5 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

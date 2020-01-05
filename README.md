
# quick_fast_api
一个开箱即用的fast api启动模板

目的为快速的fast api启动模板,并封装一些接口开发过程中,常用的方法
#### python >3.6

## 目录

- [基本的数据库访问,异步](#基本的数据库访问)
- [一个极其简单的redis key操作](#一个极其简单的redis key操作)
- [一个fast api的模块分包,可对比flask blueprint](#更大的项目)
- [一个存在小bug的日志模块](#日志模块)
- [Future](#Future)



## 基本的数据库访问
`异步mysql` 在fast api官方的demo中,就有异步的mysql操作,不过在我的一些日常使用中，仍然存在着一些问题,所以目前是在使用纯sql的情况下,建议使用异步操作,不过貌似orm现在也没有合适的异步库。

## 一个极其简单的redis key操作
`常用的缓存操作` 虽然redis有更多的使用方式,但是在目前,我所写的代码中,更多的还是基于缓存在使用

## 更大的项目
`flask blueprint` 在我从flask切换到fast api的过程中,在解决awsit和async之后,我在想要的就是类似于flask的蓝图功能,于是我找到了官方文档中的**include_router**

## 日志模块
在flask中,日志模块是由flask管理,即我用uwsgi做服务器部署,uwsgi也不做日志处理。在fast api中,通过**uvicorn**部署服务器,uvicorn也对日志层做了处理，导致在fast api内部做的日志记录会在输出层面多次数的输出。


## Future
- [ ] 更标准的日志模块
- [ ] 一个基于redis的简单路由缓存装饰器
- [ ] 同步下数据库的常用方法封装
- [ ] 类似于flask的before request和after request的封装

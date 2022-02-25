# python-flask-init

## 目標
往後建立 flask 參考專案

## Version 
1.1.20220225
## 環境

* python 3.9 以上
## How to start

* 建立虛擬環境  
```
$ python -m venv venv
# 1_create_env.sh
```

* 開啟虛擬環境
```
$ source venv/bin/activate
```

* 安裝相依
```
$ pip install -r requirement.txt
# ./3_install_dependency.sh
```

* 啟動
```
$ python app.py
# ./4_start.sh
```

* 測試
```
$ coverage run -m pytest -s -W ignore::DeprecationWarning
# ./5_test.sh
```

## 初始化
```
cd 目標資料夾
git clone git@github.com:w91379137/python-flask-init.git
cd python-flask-init
ls -la
rm -rf .git # 移除目前 git
cd ..
mv python-flask-init 專案名稱
```


## TODO

- [x] controller / get / post
- [x] middleware
- [x] log
- [x] cmd
- [x] config
- [x] db
- [x] mqtt
- [ ] web / [render_template](https://ithelp.ithome.com.tw/articles/10222132) 
- [x] test 
- [ ] swagger
- [x] [ddd](https://github.com/iktakahiro/dddpy)
- [ ] [pydash](https://github.com/dgilland/pydash)
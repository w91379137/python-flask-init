
def getValueInArgBody(request, key):

    if request.json is not None:
        # print(json.dumps(request.json))

        if key in request.json:
            return request.json[key]

    if request.args is not None:
        # print(json.dumps(request.args))
        return request.args.get(key)

def errorPrintHandle(e: BaseException):
    print(f"""
        API 錯誤:
        Error({type(e).__name__}):{e}
    """)
    
    # 如果需要看到報錯的地方請打開下一行
    # raise e
from hashlib import md5

import requests


def get_form_data(text, le):
    """
    构建表单参数
    :param :text:翻译内容
    :param :le:目标语言
    """
    # 固定值
    w = "Mk6hqtUp33DGGtoS63tTJbMUYjRrG1Lu"
    v = "webdict"
    _ = "web"

    r = text + v
    time = len(r) % 10
    o = md5(r.encode("utf-8")).hexdigest()
    n = _ + text + str(time) + w + o
    f = md5(n.encode("utf-8")).hexdigest()

    form_data = {
        "q": text,
        "le": le,
        "t": time,
        "client": _,
        "sign": f,
        "keyfrom": v,
    }
    return form_data


def translate(query, to_lan):
    """
    启动翻译
    :param query: 翻译内容
    :param to_lan: 目标语言
    :return:
    """
    # 有道词典网页请求参数
    url = "https://dict.youdao.com/jsonapi_s?doctype=json&jsonversion=4"
    form_data = get_form_data(query, to_lan)

    try:
        res = requests.post(url, data=form_data).json()
        # 取第一个网络释义
        result = res["web_trans"]["web-translation"][0]["trans"][0]["value"]
        return result
    except Exception as e:
        print("翻译失败：", e)
        return "翻译失败：" + query


if __name__ == "__main__":
    """
    # 有道词典语言选项
    lang = {
        '自动检测语言': '',
        '中英': 'en',
        '中法': 'fr',
        '中韩': 'ko',
        '中日': 'ja',
    }
    """
    word = input("请输入你要翻译的文字: ")
    # ret = translate('早上好', 'ja')
    # ret = translate('你好', 'fr')
    # ret = translate('你好', 'ko')
    # ret = translate('你好', '')
    # ret = translate('你好', 'en')
    ret = translate(word, "ja")
    print("翻译结果：\n", ret)

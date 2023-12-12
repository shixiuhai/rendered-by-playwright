import re
def parse_regular(reg:str, text:str):
    """_summary_
    解析正则规则
    Args:
        reg (str): _description_
        text (str): _description_
    """
    
    # 使用 | 分割规则字符串，并去除空字符串
    reg_list = [r.strip() for r in reg.split('|') if r.strip()]
    # 将多个正则规则编译成正则表达式对象
    compiled_patterns = [re.compile(r) for r in reg_list]
    # 遍历所有编译后的正则表达式对象，匹配文本
    matches = []
    for pattern in compiled_patterns:
        matches.extend(pattern.findall(text))
    return matches

def parse_replace(reg:str, text:str):
    """_summary_
    解析replace替换规则
    Args:
        reg (str): _description_
        text (str): _description_
    """
    '("a","b")|("c","d")'
    replace_list = reg.split("|")
    for replace_item in replace_list:
        text = text.replace(eval(replace_item)[0], eval(replace_item)[1])
    return text
    

if __name__ == "__main__":
    a_1="aaaccc"
    b= "这是一段文本，包含一些URL：https://www.example.com 和 http://example.org。"
    print(parse_replace("('a','b')|('c','d')",a_1))
    # a_1.replace("a","b")
    # print(parse_regular('https?://\S+|www\.\S+',b))

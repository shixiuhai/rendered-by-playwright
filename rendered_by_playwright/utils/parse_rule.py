import re
def parse_regular(reg:str, text:str):
    """_summary_
    解析正则规则
    Args:
        reg (str): _description_
        text (str): _description_
    """
    matches = re.findall(reg, text)
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
        text.replace(replace_item[0], replace_item[1])
    return text
    

if __name__ == "__main__":
    a="aaaccc"
    b= "这是一段文本，包含一些URL：https://www.example.com 和 http://example.org。"
    # print(parse_replace('("a","b")|("c","d")',a))
    print(parse_regular('https?://\S+|www\.\S+',b))

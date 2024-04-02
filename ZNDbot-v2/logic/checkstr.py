#文字列に読み上げ変換できない文字がないかチェックして適切な文字列を返す
import re

def CheckStr(text :str) -> str:
    context_list = [c for c in text if re.match(r"[a-zA-Z0-9あ-ん]",c)]
    context = "".join(context_list)
    return context

if __name__ == "__main__":
    print(CheckStr("あいうん公a1000"))
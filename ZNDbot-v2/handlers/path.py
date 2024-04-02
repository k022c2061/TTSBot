from pathlib import Path

class FilePathHandler:
    def __init__(self,base_directory):
        self.base_directory = Path(base_directory).resolve()

    def get_absolute_path(self,target_file_path):
        target_path = self.base_directory.joinpath(target_file_path)
        return target_path
        
    
"""
class FilePathHandlerTest:
    def __init__(self, base_directory):
        self.base_directory = Path(base_directory).resolve()
        print(self.base_directory)

    def get_relative_path(self, target_file_path):
        target_path = Path(target_file_path).resolve()
        if target_path.is_file():
            
            try:
                relative_path = target_path.relative_to(self.base_directory)
                return relative_path
            except ValueError:
                # ValueError occurs if the target file is not inside the base directory
                print("Error: Target file is not inside the base directory.")
                return None
        else:
            print("Error: Target file does not exist.")
            return None

    def normalize_path(self, file_path):
        return Path(file_path).resolve()
"""

# 使用例
if __name__ == "__main__":
    pass
    # クラスのインスタンスを作成し、基準ディレクトリを指定
    #file_handler = FilePathHandler("ZNDbot")

    # 相対パスを取得したいファイルのパスを指定
    #target_file_path = "data/user.data"

    # 相対パスを取得
    #relative_path = file_handler.get_relative_path(target_file_path)
    #if relative_path:
    #    print("相対パス:", relative_path)

    # ファイルパスを正規化
    #normalized_path = file_handler.normalize_path(target_file_path)
    #print("正規化したファイルパス:", normalized_path)

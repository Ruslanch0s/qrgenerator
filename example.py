from path import Path
from main import gen_qr_code


text = "текст для шифровки в QR код"
path_to_download = Path().joinpath("example", "example.jpg")  # Путь до фона qr кода
path_to_save = Path().joinpath("example", "example.png")  # Куда сохранять результат и под каким именем (обязательно в png)

gen_qr_code(text, path_to_download, path_to_save)
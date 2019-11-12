# Ximage

Rigaku 拡張子がimgのラウエ写真のcsv, pngへの変換

## install
```
pip install Ximage
```

## How to use
```
from Ximage import Ximg_converter
converter = Ximg_converter(path_to_img_file)
converter.to_csv()
converter.to_png()
```
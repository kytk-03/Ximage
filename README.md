# xrayimg

Rigaku 拡張子がimgのラウエ写真のcsv, pngへの変換

## install

``` bash
pip install xrayimg
```

## How to use

```python
from xrayimg import XimgConverter
converter = XimgConverter(path_to_img_file)
converter.to_csv()
converter.to_png()
```

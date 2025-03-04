# 设置变量
$PYTHON_PATH = "C:\Users\25810\AppData\Local\Programs\Python\Python312"
$SCRIPT_NAME = "linovelib_downloader"

# 删除 build 目录和 dist 目录 以及 spec 文件
Write-Output "清理中..."
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue build
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue dist
Remove-Item -Force -ErrorAction SilentlyContinue "$SCRIPT_NAME.spec"

# 打包
Write-Output "打包中..."
& "$PYTHON_PATH\Scripts\pyinstaller.exe" "$SCRIPT_NAME.py" --add-data "$PYTHON_PATH\Lib\site-packages\ddddocr\common.onnx;.\ddddocr" --add-data "$PYTHON_PATH\Lib\site-packages\onnxruntime\capi\onnxruntime_providers_shared.dll;.\onnxruntime\capi"

# 生成压缩包
Write-Output "生成压缩包中..."
Compress-Archive -Path dist\$SCRIPT_NAME\* -DestinationPath "$SCRIPT_NAME.zip" -Force

# 删除 build 目录和 dist 目录
Write-Output "清理中..."
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue build
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue dist
Remove-Item -Force -ErrorAction SilentlyContinue "$SCRIPT_NAME.spec"

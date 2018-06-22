import os
import zipfile
import sys
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED


FinalZipPath = 'D:\\py_buffer\\docx_Pro\\test3\\'   #要进行压缩的文档目录
start = FinalZipPath.rfind(os.sep) + 1
filename = 'test3.zip'  #压缩后的文件名
z = zipfile.ZipFile(filename, mode="w", compression=compression)
try:
    for dirpath,dirs,files in os.walk(FinalZipPath):
        for file in files:
            if file == filename or file == "zip.py":
                continue
            print(file)
            z_path = os.path.join(dirpath, file)
            z.write(z_path, z_path[start:])
    z.close()
except:
    if z:
        z.close()


os.rename("D:\\py_buffer\\docx_Pro\\" + 'test3.zip', "D:\\py_buffer\\docx_Pro\\" + 'test3.docx')
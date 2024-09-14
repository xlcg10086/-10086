# -*- mode: python -*-

block_cipher = None

# 应用程序的描述信息
a = Analysis(['mainwindow.py'],
             pathex=[],
             binaries=[],
             datas=[('ultralytics','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# 生成可执行文件的配置
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)


# 打包成一个文件夹的配置
coll = COLLECT(pyz,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='folder')
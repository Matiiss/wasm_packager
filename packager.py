import sys
import os
import shutil

try:
    # name = sys.argv[1]
    path_to_dir = sys.argv[1]
    output_dir = (len(sys.argv) > 2 and sys.argv[2]) or 'dist'
except IndexError:
    raise Exception('Provide the name of the directory containing package and main.py')

name = os.path.basename(path_to_dir)
# output_dir = 'dist'
dependencies = 'assets'
index_temp = f'<html><meta http-equiv="Refresh" content="0; url=\'pygame.html?org.{name}\'"/></html>'

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
shutil.copytree(dependencies, output_dir)
apk_assets = os.path.join(output_dir, 'assets')
os.mkdir(apk_assets)
path_to_assets = shutil.copytree(path_to_dir, os.path.join(apk_assets, 'assets'))

archive_output = os.path.join(output_dir, f'org.{name}.zip')
shutil.make_archive(archive_output.rsplit('.', 1)[0], 'zip', apk_assets)
shutil.rmtree(apk_assets)
os.rename(archive_output, os.path.join(output_dir, f'org.{name}.apk'))

with open(os.path.join(output_dir, 'index.html'), 'w') as index:
    index.write(index_temp)

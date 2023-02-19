import os
import sys
import subprocess

if len(sys.argv) < 2:
    sys.exit("Please specify the directory ...")

read_path = sys.argv[1]
print('Try to unzip archives recursively under the directory ' + read_path)

for root, dirs, files in os.walk(read_path):
    for name in files:
        if name.endswith('.zip') or name.endswith('.rar'):
            file_name = os.path.splitext(name)[0]
            unzippath = os.path.join(root, file_name)

            # Create Content
            if not os.path.exists(unzippath):
                os.mkdir(unzippath)
                print("Create directory:" + unzippath)

            # Unzip files
            cmdline = '7z x -y -o' + '"' + unzippath + \
                '" "' + os.path.join(root, name) + '"'
            print("Unzip: " + cmdline)
            sub = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
            sub.wait()

            # Delete unzipped zip files
            cmdline = 'del /Q ' + '"' + os.path.join(root, name) + '"'
            print("Delete: " + cmdline)
            sub = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
            sub.wait()

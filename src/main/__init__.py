import time
import os
import gzip
import shutil

import urllib.error
import urllib.request


# print(time.localtime(time.time()))
# print(time.localtime())

# print(time.strftime("%Y-%m-%d",time.localtime()))

path = r'D:\daily\URLCollection'
execute_dir = r"D:\daily\URLCollection\new"

get_yesterday = int(time.strftime("%d"))-1
gz_name = r"gurls_input.log."+time.strftime("%Y-%m-")+str(get_yesterday)+".gz"

dest_dir = os.path.join(path, gz_name)
gz_url = r"http://wtp-gn-gurls02.wrs.njdc.ispn.trendmicro.com/index.html/"+gz_name

def downloadFileFromURL(dir, URL):
    try:
        urllib.request.urlretrieve(URL, dir)
    except IOError:
        print("dest_dir is not aviliable"+dest_dir)
    except os.error.URLError as e:
        print(e.reason)
        print("error retrieving the url:"+str(URL))

def unzip_GZ(ziped_file, newlocate, gz_name):
    unziped_file = ziped_file.replace(".gz", "")
    gz_file = gzip.GzipFile(ziped_file)
    open(unziped_file, "wb").write(gz_file.read())
    gz_file.close()
    shutil.move(unziped_file, newlocate+"\\"+gz_name.replace(".gz", ""))

def deleteFile():
    print(path)
    os.remove(path+"\\"+gz_name)
    # this place you can move generated xlsx file to your directory.so don't do the delete operate
    # os.remove(execute_dir+"\\"+time.strftime("%Y%m%d")+".xlsx")
    os.remove(execute_dir+"\\"+gz_name.replace(".gz", ""))
    os.remove(execute_dir+"\\"+gz_name.replace(".gz", "_new"))

def openBat():
    batPath = r"D:\daily\URLCollection\new"
    os.chdir(batPath)
    os.system(os.path.join(batPath, "new.bat"))

downloadFileFromURL(dest_dir, gz_url)
unzip_GZ(dest_dir, execute_dir, gz_name)
openBat()
time.sleep(1)
deleteFile()


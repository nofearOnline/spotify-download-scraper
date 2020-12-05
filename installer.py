import os
import platform
from zipfile import ZipFile
if "Windows" in platform.platform():
    import urllib.request


def check_if_in_path():
    """
    check if the ffmpeg bin folder is in the path

    :return:
    """
    path = os.getenv('PATH')
    if "ffmpeg" not in path:
        print("not in path, adding it to path")
        os.system('SETX PATH "%PATH%;{0}" '.format(r"C:\ffmpeg\bin"))
    else:
        print("already in path")


def check_if_downloaded() :
    """
    check if the files required are downloaded and if not it downloading and preparing it.

    :return:
    """
    if "Windows" in platform.platform():
        if not os.path.exists(r"C:\ffmpeg\bin"):
            print("downloading and installing")
            print("downloading...")
            url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.zip"
            # downloading the zip file
            urllib.request.urlretrieve(url, r"C:\ffmpeg.zip")
            print("download complete")
            # unzipping
            with ZipFile(r"C:\ffmpeg.zip", 'r') as zipObj:
                zipObj.extractall(r"c:\\")
            folders = os.listdir(r"C:\\")
            # locates and renames folders to the correct name
            for folder in folders:
                if "ffmpeg-" in folder:
                    os.replace(r"C:\\" + str(folder), r"C:\ffmpeg")
                    break
        else:
            print("already downloaded")
    elif "Linux" in platform.platform():
        pm = find_package_manager()
        if pm == "apt":
            os.system(r'sudo add-apt-repository ppa:mc3man/trusty-media; sudo apt-get update \
            sudo apt-get install -y ffmpeg;')
        elif pm == "deb":
            dist = input("enter your distribution: (‘stretch‘, ‘jessie‘, or ‘wheezy‘)")
            os.system(
                r'echo deb http://www.deb-multimedia.org {0} main non-free deb-src http://www.deb-multimedia.org {0} \
                main non-free >> /etc/apt/sources.list'.format(dist))
            os.system(r'sudo apt-get update; sudo apt-get install -y deb-multimedia-keyring; sudo apt-get update;  \
            sudo apt-get install -y ffmpeg')
        elif pm == "yum":
            os.system(r'yum install -y epel-release; yum localinstall -y --nogpgcheck \
            https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm \
            https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm')
            os.system(r'yum install -y ffmpeg ffmpeg-devel')
        elif pm == 'dnf':
            os.system(r'sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm \
            -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E \
            %fedora).noarch.rpm; sudo dnf install -y ffmpeg ffmpeg-devel')
    elif "macos" in platform.platform().lower():
        os.system(r'brew install ffmpeg')


def find_package_manager():
    usr_bin = os.listdir('/usr/bin')
    if "yum" in usr_bin:
        return "yum"
    elif "apt" in usr_bin:
        return "apt"
    elif "deb" in usr_bin:
        return "deb"
    elif "dnf" in usr_bin:
        return "dnf"


def install_deps():
    os.system(r"pip3 install -r requirements.txt")


check_if_downloaded()
install_deps()
if "Windows" in platform.platform():
    check_if_in_path()
print("INSTALLED - enjoy")

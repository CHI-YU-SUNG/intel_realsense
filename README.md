# Intel_realsense
The method for user to use intel-realsens
* Calibration
* Save RGB and Depth video on real time
## Environment setting
* Step 1: Add Intel server to the list of repositories :\
$ echo 'deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo xenial main' | sudo tee /etc/apt/sources.list.d/realsense-public.list
* Step 2: Register the server’s public key :\
  $ sudo apt-key adv --keyserver keys.gnupg.net --recv-key 6F3EFCDE
* Step 3: Refresh the list of repositories and packages available
* Step 4: In order to run demos install:
* Test: realsense-viewe
## Usage
## Demo
### Reference
* [official github](https://github.com/IntelRealSense/librealsense/releases)

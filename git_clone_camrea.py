#! /usr/bin/env python
##############################################################################
#
#	CopyRight		(C)	2025,VIVO			All Right Reserved!
#
#	Module:		git clone <camera repo>
#
#	File:		git_clone_camera.sh
#
#	Author:		liuchangjian
#
#	Date:		2015-10-19
#
#	E-mail:		liuchangjian@vivo.com.cn
#
################################################################################

################################################################################
#
#	History:
#
#	Name				Date			Ver			Act
#----------------------------------------------------------------------
#	liuchangjian		2015-10-19		v0.1		create
#	liuchangjian		2015-11-09		v0.2		add git fetch cmd!
#
#################################################################################

import os,sys

# global var
ard_version=2
platform=3
repos=[]

# git info
username="liuchangjian"
git_cmd="git clone "
url="ssh://"+username+"@smartgit:29418/"


# Android 5.0 camera repos
camera_50_com_repos=(
	"ard_5.0/android_frameworks_base",
	"ard_5.0/android_frameworks_av",
	"ard_5.0/android_kernel"
)

camera_50_mtk_repos=(
	"ard_5.0/android_vendor_mediatek_proprietary_custom",
	"ard_5.0/android_vendor_mediatek_proprietary_hardware",
	"ard_5.0/android_vendor_mediatek_proprietary_platform"
)

camera_50_qcom_repos=(
	"ard_5.0/android_hardware_qcom_camera",
	"ard_5.0/android_vendor_qcom_proprietary_mm-camera",
)

# Android 5.0 camera repos
camera_51_com_repos=(
	"ard_5.1/android_frameworks_base",
	"ard_5.1/android_frameworks_av",
	"ard_5.1/android_kernel"
)

camera_51_mtk_repos=(
	"ard_5.1/android_vendor_mediatek_proprietary_custom",
	"ard_5.1/android_vendor_mediatek_proprietary_hardware",
	"ard_5.1/android_vendor_mediatek_proprietary_platform"
)

camera_51_qcom_repos=(
	"ard_5.1/android_hardware_qcom_camera",
	"ard_5.1/android_vendor_qcom_proprietary_mm-camera",
)

# Android 6.0 camera repos
camera_60_com_repos=(
	"ard_6.0/android_frameworks_base",
	"ard_6.0/android_frameworks_av",
	"ard_6.0/android_kernel"
)

camera_60_mtk_repos=(
	"ard_6.0/android_vendor_mediatek_proprietary_custom",
	"ard_6.0/android_vendor_mediatek_proprietary_hardware",
	"ard_6.0/android_vendor_mediatek_proprietary_platform"
)

camera_60_qcom_repos=(
	"ard_6.0/android_hardware_qcom_camera",
	"ard_6.0/android_vendor_qcom_proprietary_mm-camera",
)

def ReposSelect(ver,plt):
	if ver == 1:
		if not os.path.exists("ard_5.0"):
			os.mkdir("ard_5.0")
		os.chdir("ard_5.0")
		com=camera_50_com_repos
		mtk=camera_50_mtk_repos
		qcom=camera_50_qcom_repos
	elif ver == 2:
		if not os.path.exists("ard_5.1"):
			os.mkdir("ard_5.1")
		os.chdir("ard_5.1")
		com=camera_51_com_repos
		mtk=camera_51_mtk_repos
		qcom=camera_51_qcom_repos
	elif ver == 3:
		if not os.path.exists("ard_6.0"):
			os.mkdir("ard_6.0")
		os.chdir("ard_6.0")
		com=camera_60_com_repos
		mtk=camera_60_mtk_repos
		qcom=camera_60_qcom_repos
	else:
		print "ver num:",ver,"is ERROR!!!"

	PlatSelect(plt,com,mtk,qcom)

def PlatSelect(plt,com_r,mtk_r,qcom_r):
	repos.extend(com_r)
	if plt == 1:
		repos.extend(mtk_r)
	elif plt == 2:
		repos.extend(qcom_r)
	elif plt == 3:
		repos.extend(mtk_r)
		repos.extend(qcom_r)
	else:
		print "platform num:",plt,"is ERROR!!!"

def CamReposClone(repos):
	for x in repos:
		a_ver,dir = x.split("/")
		if not os.path.exists(dir):
			cmd = git_cmd+url+x
			print "git: ",cmd
			os.system(cmd)
		else:
			cmd = "git fetch"
			print cmd+" "+x
			os.chdir(dir)
			os.system(cmd)
			os.chdir("..")
	

def ParseArgv():
	if not len(sys.argv):
		return

	for i in range(1,len(sys.argv)):
		if sys.argv[i] == '-h':
			Usage()
			sys.exit()
		elif sys.argv[i] == '-a':
			if sys.argv[i+1]:
				version = string.atoi(sys.argv[i+1],10)
				if type(version) == int:
					global ard_version
					ard_version = version						
				else:
					print 'cmd para ERROR: '+sys.argv[i+1]+' is not int num!!!'
			else:
				Usage()
				sys.exit()
		elif sys.argv[i] == '-p':
			if sys.argv[i+1]:
				plat = string.atoi(sys.argv[i+1],10)
				if type(w_num) == int:
					global platform
					platform = plat						
				else:
					print 'cmd para ERROR: '+sys.argv[i+1]+' is not int num!!!'
			else:
				Usage()
				sys.exit()
		else:
				Usage()
				sys.exit()
					

def Usage():
	print 'Command Format :'
	print '		git_clone_camera.py '
	print '							[-a 1(Android 5.0)/2(Android 5.1)/3(Android 6.0)] [-p 1(mtk)/2(qcom)/3(mtk+qcom)]| [-h]'


if __name__ == '__main__':

	ParseArgv()
	
	ReposSelect(ard_version,platform)
	
	CamReposClone(repos)
	
	print "\nCamera Repos Clone is OK! And Exit()!\n"

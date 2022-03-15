import argparse, sys
from DOCKER.DOCKER_HANDLER import docker
from COMANDER.GENERIC_MQTT import Generic_Mqtt
docker = docker()
mqtt = Generic_Mqtt()
#imagename = "pythonimage7"
amd_architecture = "amd64"
arm32v7_architecture = "arm32v7"
arm64_architecture = "arm64"
argParser = argparse.ArgumentParser()
argParser.add_argument("--arch", metavar="arm32v7/amd64/arm64",help="architecture")
argParser.add_argument("--build", metavar="start", help="build module")
argParser.add_argument("--push", metavar="start", help="push to hub")
argParser.add_argument("--deploy",metavar="start", help="deploye module")
argParser.add_argument("--name", metavar="xyz", help="name of module")
#argParser.add_argument("--version", help="container version")
args = argParser.parse_args()
print("args=%s" % args)

if args.build == "start":
    docker.get_version()
    try:
        if args.arch == arm32v7_architecture:
            check_build = docker.build_image(args.module_name,arm32v7_architecture)
            print(check_build)
        if args.arch == amd_architecture:
            check_build = docker.build_image(args.module_name,amd_architecture)
            print(check_build)
        if args.arch == arm64_architecture:
            check_build = docker.build_image(args.module_name,arm64_architecture)
            print(check_build)
        else:
            print("Please enter correct architecture for successfully build")
    except:
        e = sys.exc_info()[0]
        print("build failed")
        pass
if args.push == "start":
    print("pushing the image....")
    check_push = docker.push_image(args.name)
    if check_push:
        print("push success")
    else:
        print("push failed")
    
if args.deploy == "start":
    print("deploying the image....")
    

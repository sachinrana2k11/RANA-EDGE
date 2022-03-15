import os
#docker buildx build -t andrewlock/wait-for-dependencies:latest --platform linux/amd64,linux/arm64,linux/ppc64le,linux/s390x,linux/386,linux/arm/v7,linux/arm/v6 .
class docker():
    def __init__(self):
        self.username = "sachinrana2k11"

    def get_version(self):
        os.system("docker -v")
        #os.system("pip3 freeze > MAIN_CODE\requirements.txt")
    
    def build_image(self, image_name, architecture):
        try:
            print("building start wait....")
            if architecture == "arm32v7":
                temp = os.system("docker build --rm -f DOCKER\DOCKERFILES\Dockerfile.arm32v7 --platform linux/arm/v7 -t "+self.username+"/"+image_name+" MAIN_CODE")
                return temp
            if architecture == "amd64":
                os.system("docker build --rm -fDOCKER\DOCKERFILES\Dockerfile.amd64 --platform linux/amd64 -t "+self.username+"/"+image_name+" MAIN_CODE")
                return True
            if architecture == "arm64":
                os.system("docker build --rm -f DOCKER\DOCKERFILES\Dockerfile.arm64v8 --platform linux/arm64 -t "+self.username+"/"+image_name+" MAIN_CODE")
                return True
        except:
            print("Error in building the image")
            return False
    def push_image(self, name):
        try:
            print("pushing start wait....")
            os.system("docker push "+self.username+"/"+name)
            return True
        except:
            print("Error in pushing the image")
            return False
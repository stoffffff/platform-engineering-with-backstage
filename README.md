# platform-engineering-with-backstage
# STEPS<br>
# Setup | Foundamentals of DevOps
- Write a flask app code. ✅​<br>
- Build it as a docker Image. ✅​ <br> 
***docker build -t stoffffff/python-stof:v1 .***<br>
- Deploy it on an Ubuntu VM as a container. ✅​<br> 
***docker run -d -p 8080:5000 stoffffff/python-stof:v1***<br>
***check it up at: http:YOUR_VM_IP:8080/main***<br>
- Build newer versions and redeploy.✅​<br>

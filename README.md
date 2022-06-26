# ML_project_class
"First class End to end Project"

Creating Conda Environment

```
conda create -p venv python==3.7 -y
conda activate venv/
```

Git Commands:
```
add file in git : git add filename or git add .
to check added file : git status
to commit: git commit -m "message"
to push change to main: git push origin main

to check urls : git remote -v
to Restore : git restore file_name
to see all the version : git log
```
BUILD DOCKER IMAGE
```
docker image : docker build -t <image_name>:<tagname> .
List Docker Images : docker images

run docker: docker run -p 5000:5000 -e PORT=5000 85077eef823f

to check running containers: docker ps

to stop container : docker stop <container_id>

```

to install requirements.
```
  python setup.py install  
```
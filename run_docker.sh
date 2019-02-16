xhost +local:docker

docker run -ti --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /home/threefrog/Git/ros_workshop:/root \
    --name ros_workshop ros:kinetic-full 


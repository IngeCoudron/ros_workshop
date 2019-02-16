xhost +local:docker

docker run -ti --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /home/inge/Git/ros_workshop:/tmp \
    --name ros_workshop ros:kinetic-full 


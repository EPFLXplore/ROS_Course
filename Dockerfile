###########################################
# Xplore Course image
###########################################
FROM ghcr.io/epflxplore/docker_commons:humble-desktop

################################## JUPYTERLAB ##################################

ARG DEBIAN_FRONTEND=noninteractive



RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends && \
    apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
    && apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
    locales cmake git build-essential \
    python3-pip python3-setuptools python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install --upgrade pip setuptools \
    && python3 -m pip install jupyterlab==0.35.4 bash_kernel==0.7.1 tornado \
    && python3 -m bash_kernel.install

EXPOSE 8888

###################################### ROS #####################################

USER $USERNAME

# Install extra ROS packages
RUN pip3 install pyyaml rospkg jupyros==0.7.0a0

WORKDIR /home/$USERNAME/ros-jupyter

COPY . .

CMD ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--NotebookApp.token=''", "--allow-root"]

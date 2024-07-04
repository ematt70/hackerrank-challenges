FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

COPY ./requirements.txt /tmp/requirements.txt

RUN sudo apt-get update && apt-get upgrade -y && apt-get install -y xz-utils python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install -r /tmp/requirements.txt

COPY ./.devcontainer/scripts/git_aliases.sh /etc/profile.d/git_aliases.sh
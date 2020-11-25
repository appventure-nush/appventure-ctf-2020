FROM python:3

RUN apt-get update
RUN apt-get install bash netcat-openbsd curl nano vim build-essential openssh-server binwalk -y

RUN adduser \
    --disabled-password \
    --gecos "" \
    --shell /bin/bash \
    appventure

RUN echo "appventure:appventure" | chpasswd

USER appventure

RUN pip3 install pwntools

USER root

COPY sshd_config /etc/ssh/sshd_config

RUN mkdir -p /var/run/sshd

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

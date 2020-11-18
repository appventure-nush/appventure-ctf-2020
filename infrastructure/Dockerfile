FROM alpine

RUN apk --update add --no-cache openssh bash netcat-openbsd curl nano vim python3
RUN /usr/bin/ssh-keygen -A
RUN ssh-keygen -t rsa -b 4096 -f  /etc/ssh/ssh_host_key

RUN adduser \
    --disabled-password \
    --gecos "" \
    --shell /bin/bash \
    appventure

RUN echo "appventure:appventure" | chpasswd
COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

FROM python:3

RUN apt-get update && apt-get install xinetd -y
COPY ctf.xinetd /etc/xinetd.d/ctf

RUN useradd -ms /bin/bash ctf
USER ctf
COPY --chown=ctf:root . .


CMD ["xinetd", "-dontfork"]
EXPOSE 4200

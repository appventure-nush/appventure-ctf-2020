FROM python:3

RUN apt-get update && apt-get install xinetd g++ -y
COPY ctf.xinetd /etc/xinetd.d/ctf

RUN useradd -ms /bin/bash ctf
USER ctf
COPY --chown=ctf:root . .
RUN g++ solution.cpp -o solution


CMD ["xinetd", "-dontfork"]
EXPOSE 4200

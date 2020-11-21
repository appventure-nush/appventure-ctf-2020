FROM python:3

RUN apt-get update && apt-get install xinetd -y
COPY ctf.xinetd /etc/xinetd.d/ctf

RUN useradd -ms /bin/bash ctf

RUN mkdir chal
WORKDIR chal
COPY . .
RUN rm *.md
RUN chmod -w *

USER ctf

CMD ["xinetd", "-dontfork"]
EXPOSE 1236

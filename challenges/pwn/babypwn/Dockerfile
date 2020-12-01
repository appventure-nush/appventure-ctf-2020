FROM ubuntu:16.04
ENV user ctf
ENV chal babypwn

# Run Updates
RUN apt-get -y update
RUN apt-get install -y socat

# Create User
RUN useradd -m $user
WORKDIR /home/$user

# Set Files
COPY babypwn /home/$user
COPY flag /home/$user
RUN rm -rf /home/$user/.bashrc /home/$user/.profile /home/$user/.bash_logout

RUN chown -R root /home/$user/
RUN chmod 641 /home
RUN chgrp $user /home/$user/$chal
RUN chmod 555 /home/$user/$chal

CMD socat TCP-LISTEN:4200,reuseaddr,fork EXEC:/home/$user/$chal
USER $user
EXPOSE 4200

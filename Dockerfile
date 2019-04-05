FROM debian:stretch-slim

RUN apt-get update
RUN apt-get install -y avahi-utils python3-pip python3-zmq python3-gevent
RUN pip3 install zerorpc

COPY pmc-health /root
COPY start.sh /root

ENTRYPOINT ["/root/start.sh"]

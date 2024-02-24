FROM pramodraob/hadoop-base:latest

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

RUN mkdir /input
COPY input/input.txt /input/

COPY mapper.py /mapper.py
COPY reducer.py /reducer.py

ADD runner-script /runner-script
RUN chmod a+x /runner-script

CMD ["/runner-script    \
            /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
            /input/input.txt     \
            /input/     \
            /output/"]
FROM pramodraob/hadoop-base:latest

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

RUN mkdir /input
ADD input /input/

COPY mapper0.py /mapper0.py
COPY reducer0.py /reducer0.py

COPY mapper1.py /mapper1.py
COPY reducer1.py /reducer1.py

COPY mapper2.py /mapper2.py
COPY reducer2.py /reducer2.py

ADD runner-script /runner-script
RUN chmod a+x /runner-script

CMD ["/runner-script    \
            /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
            /input/    \
            in      \
            out"]
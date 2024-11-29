# Resume in LateX
# Adapted Dockerfile made by Sourabh Bajaj for my own used case
# https://github.com/sb2nov/resume/blob/master/Dockerfile


FROM debian:stable-slim
ENV DEBIAN_FRONTEND=noninteractive

RUN echo "deb http://deb.debian.org/debian stable main" > /etc/apt/sources.list && \
    echo "deb http://deb.debian.org/debian stable-updates main" >> /etc/apt/sources.list && \
    echo "deb http://deb.debian.org/debian-security stable-security main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -qyf \
    curl jq make git \
    python3 python3-jinja2 \
    python3-pygments gnuplot \
    biber \
    latexmk \
    texlive-full \
    texlive-fonts-extra \
    texlive-fonts-recommended
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]

COPY prepare_resume.py /usr/local/bin
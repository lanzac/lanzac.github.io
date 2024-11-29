# Docker Image for convertion from JsonResume to LaTeX PDF

This repository provides a Docker image for working with LaTeX. You can use this image to compile LaTeX documents without the need to install LaTeX locally.
Current Version: v0.04

## Build the Docker Image

To build the Docker image locally, run the following command:

    docker build -t andrelanrezac/latex:v0.04 .


This will build the image and tag it as `andrelanrezac/latex:v0.04`.

After building the image, you can push it to Docker Hub:

    docker push andrelanrezac/latex:v0.04

## Use locally

To use the LaTeX image for compiling documents, run the following command:

    docker run --rm -it -v "$PWD":/data andrelanrezac/latex:v0.04

This will mount your current working directory ($PWD) to the /data directory inside the container, and allow you to compile LaTeX files.


Example Workflow (please find commands in `.github/workflows/jsonresume.yml`)

    python3 /usr/local/bin/prepare_resume.py assets/json/resume_en-us.json assets/tex/template_resume.tex -o assets/tex/resume_en-us.tex

    lualatex -output-directory=assets/pdf/en-us assets/tex/resume_en-us.tex

    biber assets/pdf/en-us/resume_en-us.bcf
    
    lualatex -output-directory=assets/pdf/en-us assets/tex/resume_en-us.tex

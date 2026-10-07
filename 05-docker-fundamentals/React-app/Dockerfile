FROM node:14 as build
WORKDIR /app
# Mock build
RUN echo "building react"
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
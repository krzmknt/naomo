FROM nginx:1.13.1-alpine
COPY work/nginx.conf /etc/nginx
RUN apk --no-cache add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata
CMD ["nginx", "-g", "daemon off;"]

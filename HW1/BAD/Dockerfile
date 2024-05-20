# использовать apt-get внутри dockerfile - плохо
FROM busybox:1.24

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  g++ \
  gcc \
  libc6-dev \
  make \
  && rm -rf /var/lib/apt/lists/*

# мы сначала берем вообще весь архив
ADD example.tar.gz /add 

# а потом вообще все копируем
COPY example.tar.gz /copy 

# плохо потому, что, возможно, нам нужно только что то конкрутное из архива

# плохо использовать тэг latest, потмоу что нет четкой привязи к версии
# возможна несовремтимость чего-то в дальшейшем
FROM node:latest

# без комментариев
ENV MY_SECRET_PASSRORD 123456

# использование раздельных команд, когда их млжно логически разделить редет к увеличению колл-ва слоев 
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz
RUN echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c -
RUN tar -C /usr/local -xzf golang.tar.gz
RUN rm golang.tar.gz

# правильно будет так 
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
 && echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
 && tar -C /usr/local -xzf golang.tar.gz \
 && rm golang.tar.gz
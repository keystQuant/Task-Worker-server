FROM node:8
RUN npm install -g pm2
COPY . /src
WORKDIR /src
RUN npm install
RUN node init.js
EXPOSE 8080
CMD pm2 start --no-daemon socket.js

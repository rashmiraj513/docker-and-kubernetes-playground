FROM node:18


WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ARG DEFAULT_PORT=80

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

VOLUME [ "/app/node_modules", "/app/temp" ]

CMD ["npm", "start"]

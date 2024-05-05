FROM node:20-alpine

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

RUN npm build

EXPOSE 3000

CMD ["npm", "serve", "--port", "3000"]
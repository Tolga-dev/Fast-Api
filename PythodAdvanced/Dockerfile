﻿FROM node


WORKDIR /user/src/app

COPY package.json ./ 
RUN npm install

COPY . . 

EXPOSE 4000

CMD ["npm", "start"]


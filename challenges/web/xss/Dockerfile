FROM zenika/alpine-chrome:with-puppeteer

RUN mkdir chal
WORKDIR chal
COPY . .
RUN npm ci

CMD ["node","index.js"]

EXPOSE 1238

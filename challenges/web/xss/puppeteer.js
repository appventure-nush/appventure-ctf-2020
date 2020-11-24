const puppeteer = require("puppeteer");

async function visitUrl(url, cookies) {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.setCookie(...cookies);
  await page.goto(url);
  setTimeout(async () => {
    await browser.close();
  }, 1000);
}


module.exports = visitUrl;

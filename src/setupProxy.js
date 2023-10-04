const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = (app) => {

    app.use(
        '/v1/search',
        createProxyMiddleware({
            target: 'https://openapi.naver.com',
            // ws: true,
            changeOrigin: true,
        })
    );
};

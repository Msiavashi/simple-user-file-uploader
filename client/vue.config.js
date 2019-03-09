module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000/',
                changeOrigin: true
            },
            '/user': {
                target: 'http://localhost:8000/',
                changeOrigin: true
            }
        }
    }
}
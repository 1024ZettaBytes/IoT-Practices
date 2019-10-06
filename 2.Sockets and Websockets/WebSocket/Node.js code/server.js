const app = require('express')();
const appWs = require('express-ws')(app);

app.ws('/wsESP32', ws => {
    console.log("[*] ESP32 conectado!");
    ws.on('message', msg => {
        console.log('Mensaje recibido: ', msg);
    });
});

app.listen(999, () => console.log('[*] Servidor inicializado! Esperando conexión...'));
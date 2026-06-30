const banco = require('mongoose');

banco.connect('mongodb://127.0.0.1:27017/livraria')
  .then(() => console.log('Conectado ao MongoDB com sucesso.'))
  .catch((err) => console.error('Erro ao conectar ao MongoDB:', err));

module.exports = banco;

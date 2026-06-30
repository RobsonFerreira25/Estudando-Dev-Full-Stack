const banco = require('./conexao');

const LivroSchema = new banco.Schema({
  titulo: { type: String, required: true },
  resumo: { type: String, required: true },
  autores: { type: [String], required: true },
  codEditora: { type: Number, required: true }
});

const Livro = banco.model('Livro', LivroSchema, 'livros');

// Semear banco de dados se estiver vazio
Livro.countDocuments().then(async (count) => {
  if (count === 0) {
    await Livro.create([
      { titulo: 'Livro de Angular', resumo: 'Aprendendo Angular passo a passo.', codEditora: 1, autores: ['John Doe'] },
      { titulo: 'Guia do React', resumo: 'Tudo sobre React.', codEditora: 2, autores: ['Jane Doe', 'Mary Smith'] },
      { titulo: 'Vue JS Prático', resumo: 'Criando aplicações com Vue.', codEditora: 3, autores: ['Peter Jones'] }
    ]);
    console.log('Banco de dados inicializado com livros padrão!');
  }
}).catch(err => {
  console.log('Erro ao inicializar dados padrão (certifique-se de que o MongoDB está em execução):', err.message);
});

module.exports = Livro;

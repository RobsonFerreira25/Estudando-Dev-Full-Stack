const express = require('express');
const router = express.Router();
const { obterLivros, incluir, excluir } = require('../modelo/livro-dao');

// GET - Retorna a lista de todos os livros
router.get('/', async (req, res) => {
  try {
    const livros = await obterLivros();
    res.json(livros);
  } catch (error) {
    res.status(500).json({ ok: false, mensagem: 'Erro ao obter os livros', erro: error.message });
  }
});

// POST - Inclui um novo livro no banco de dados
router.post('/', async (req, res) => {
  try {
    await incluir(req.body);
    res.json({ ok: true, mensagem: 'Livro incluído com sucesso!' });
  } catch (error) {
    res.status(400).json({ ok: false, mensagem: 'Falha ao incluir o livro', erro: error.message });
  }
});

// DELETE - Exclui um livro pelo seu _id
router.delete('/:id', async (req, res) => {
  try {
    const codigo = req.params.id;
    const resultado = await excluir(codigo);
    if (resultado.deletedCount > 0) {
      res.json({ ok: true, mensagem: 'Livro excluído com sucesso!' });
    } else {
      res.status(404).json({ ok: false, mensagem: 'Livro não encontrado' });
    }
  } catch (error) {
    res.status(500).json({ ok: false, mensagem: 'Falha ao excluir o livro', erro: error.message });
  }
});

module.exports = router;

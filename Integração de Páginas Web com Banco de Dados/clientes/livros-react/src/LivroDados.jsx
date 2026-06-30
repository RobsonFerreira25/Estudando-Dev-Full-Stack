import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ControleLivros } from './controle/ControleLivros';
import { ControleEditora } from './controle/ControleEditora';
import { Livro } from './model/Livro';

const controleLivros = new ControleLivros();
const controleEditora = new ControleEditora();

export default function LivroDados() {
  const navigate = useNavigate();
  const editoras = controleEditora.getEditoras();

  const [titulo, setTitulo] = useState('');
  const [resumo, setResumo] = useState('');
  const [codEditora, setCodEditora] = useState(editoras[0] ? editoras[0].codEditora : 0);
  const [autores, setAutores] = useState('');

  const incluir = (event) => {
    event.preventDefault();
    const autoresArray = autores.split('\n').filter((a) => a.trim() !== '');
    // Criando o objeto Livro com código vazio conforme instruções
    const livro = new Livro('', Number(codEditora), titulo, resumo, autoresArray);

    controleLivros.incluir(livro).then(() => {
      navigate('/');
    });
  };

  return (
    <main className="container mt-4">
      <h1>Dados do Livro</h1>
      <form onSubmit={incluir} className="mt-3">
        <div className="mb-3">
          <label htmlFor="titulo" className="form-label">Título</label>
          <input
            type="text"
            className="form-control"
            id="titulo"
            value={titulo}
            onChange={(e) => setTitulo(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="resumo" className="form-label">Resumo</label>
          <textarea
            className="form-control"
            id="resumo"
            rows="3"
            value={resumo}
            onChange={(e) => setResumo(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="codEditora" className="form-label">Editora</label>
          <select
            className="form-select"
            id="codEditora"
            value={codEditora}
            onChange={(e) => setCodEditora(Number(e.target.value))}
          >
            {editoras.map((editora) => (
              <option key={editora.codEditora} value={editora.codEditora}>
                {editora.nome}
              </option>
            ))}
          </select>
        </div>

        <div className="mb-3">
          <label htmlFor="autores" className="form-label">Autores (1 por linha)</label>
          <textarea
            className="form-control"
            id="autores"
            rows="3"
            value={autores}
            onChange={(e) => setAutores(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="btn btn-primary">Salvar Dados</button>
      </form>
    </main>
  );
}

import React, { useState } from 'react';
import Head from 'next/head';
import Router from 'next/router';
import { Menu } from '../componentes/Menu';
import { ControleLivros } from '../classes/controle/ControleLivros';
import { ControleEditora } from '../classes/controle/ControleEditora';
import { Livro } from '../classes/model/Livro';

const controleLivros = new ControleLivros();
const controleEditora = new ControleEditora();

export default function LivroDados() {
  const editoras = controleEditora.getEditoras();

  const [titulo, setTitulo] = useState('');
  const [resumo, setResumo] = useState('');
  const [codEditora, setCodEditora] = useState(editoras[0] ? editoras[0].codEditora : 0);
  const [autores, setAutores] = useState('');

  const incluir = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const autoresArray = autores.split('\n').filter((a) => a.trim() !== '');
    // Instanciar o Livro com o código vazio para MongoDB
    const livro = new Livro('', Number(codEditora), titulo, resumo, autoresArray);

    controleLivros.incluir(livro).then(() => {
      Router.push('/LivroLista');
    });
  };

  return (
    <div className="min-vh-100 bg-light">
      <Head>
        <title>Novo Livro - Next.js</title>
      </Head>

      <Menu />

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
              rows={3}
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
              rows={3}
              value={autores}
              onChange={(e) => setAutores(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn btn-primary">Salvar Dados</button>
        </form>
      </main>
    </div>
  );
}

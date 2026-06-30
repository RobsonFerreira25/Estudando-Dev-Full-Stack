import React, { useState, useEffect } from 'react';
import Head from 'next/head';
import { Menu } from '../componentes/Menu';
import { ControleLivros } from '../classes/controle/ControleLivros';
import { ControleEditora } from '../classes/controle/ControleEditora';
import { Livro } from '../classes/model/Livro';

const controleLivros = new ControleLivros();
const controleEditora = new ControleEditora();

interface LinhaLivroProps {
  livro: Livro;
  excluir: (codigo: string) => void;
}

export const LinhaLivro: React.FC<LinhaLivroProps> = (props) => {
  const { livro, excluir } = props;
  const nomeEditora = controleEditora.getNomeEditora(livro.codEditora);

  return (
    <tr>
      <td>
        {livro.titulo}
        <br />
        <button className="btn btn-danger btn-sm mt-2" onClick={() => excluir(livro.codigo)}>
          Excluir
        </button>
      </td>
      <td>{livro.resumo}</td>
      <td>{nomeEditora}</td>
      <td>
        <ul>
          {livro.autores.map((autor, idx) => (
            <li key={idx}>{autor}</li>
          ))}
        </ul>
      </td>
    </tr>
  );
};

export default function LivroLista() {
  const [livros, setLivros] = useState<Array<Livro>>([]);
  const [carregado, setCarregado] = useState(false);

  useEffect(() => {
    if (!carregado) {
      controleLivros.obterTodos().then((resultado) => {
        setLivros(resultado);
        setCarregado(true);
      });
    }
  }, [carregado]);

  const excluir = (codigo: string) => {
    controleLivros.excluir(codigo).then(() => {
      setCarregado(false);
    });
  };

  return (
    <div className="min-vh-100 bg-light">
      <Head>
        <title>Catálogo de Livros - Next.js</title>
      </Head>

      <Menu />

      <main className="container mt-4">
        <h1>Catálogo de Livros</h1>
        <table className="table table-striped table-hover mt-3">
          <thead className="table-dark">
            <tr>
              <th scope="col">Título</th>
              <th scope="col">Resumo</th>
              <th scope="col">Editora</th>
              <th scope="col">Autores</th>
            </tr>
          </thead>
          <tbody>
            {livros.map((livro, index) => (
              <LinhaLivro
                key={index}
                livro={livro}
                excluir={excluir}
              />
            ))}
          </tbody>
        </table>
      </main>
    </div>
  );
}

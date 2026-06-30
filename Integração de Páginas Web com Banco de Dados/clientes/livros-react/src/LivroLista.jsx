import React, { useState, useEffect } from 'react';
import { ControleLivros } from './controle/ControleLivros';
import { ControleEditora } from './controle/ControleEditora';

const controleLivros = new ControleLivros();
const controleEditora = new ControleEditora();

export const LinhaLivro = (props) => {
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
  const [livros, setLivros] = useState([]);
  const [carregado, setCarregado] = useState(false);

  useEffect(() => {
    if (!carregado) {
      controleLivros.obterTodos().then((resultado) => {
        setLivros(resultado);
        setCarregado(true);
      });
    }
  }, [carregado]);

  const excluir = (codigo) => {
    controleLivros.excluir(codigo).then(() => {
      setCarregado(false);
    });
  };

  return (
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
              key={index} // Adicionado o index como key por ser numérico, enquanto o código agora é textual
              livro={livro}
              excluir={excluir}
            />
          ))}
        </tbody>
      </table>
    </main>
  );
}

import { Livro } from '../model/Livro';

const baseURL = "http://localhost:3030/livros";

export interface LivroMongo {
  _id: string | null;
  codEditora: number;
  titulo: string;
  resumo: string;
  autores: string[];
}

export class ControleLivros {
  async obterLivros(): Promise<Array<Livro>> {
    const response = await fetch(baseURL);
    const data: Array<LivroMongo> = await response.json();
    return data.map(item => new Livro(
      item._id || '',
      item.codEditora,
      item.titulo,
      item.resumo,
      item.autores
    ));
  }

  async obterTodos(): Promise<Array<Livro>> {
    return this.obterLivros();
  }

  async incluir(livro: Livro): Promise<boolean> {
    const livroMongo: LivroMongo = {
      _id: null,
      codEditora: livro.codEditora,
      titulo: livro.titulo,
      resumo: livro.resumo,
      autores: livro.autores
    };

    const response = await fetch(baseURL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(livroMongo)
    });
    const result = await response.json();
    return result.ok;
  }

  async excluir(codigo: string): Promise<boolean> {
    const response = await fetch(`${baseURL}/${codigo}`, {
      method: 'DELETE'
    });
    const result = await response.json();
    return result.ok;
  }
}

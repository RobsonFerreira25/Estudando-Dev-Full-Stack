import { Injectable } from '@angular/core';
import { Livro } from './livro';

@Injectable({
  providedIn: 'root'
})
export class ControleLivrosService {
  private livros: Array<Livro> = [
    { codigo: 1, codEditora: 1, titulo: 'Livro de Angular', resumo: 'Aprendendo Angular passo a passo.', autores: ['John Doe'] },
    { codigo: 2, codEditora: 2, titulo: 'Guia do React', resumo: 'Tudo sobre React.', autores: ['Jane Doe', 'Mary Smith'] },
    { codigo: 3, codEditora: 3, titulo: 'Vue JS Prático', resumo: 'Criando aplicações com Vue.', autores: ['Peter Jones'] }
  ];

  constructor() { }

  obterLivros(): Array<Livro> {
    return this.livros;
  }

  incluir(livro: Livro): void {
    const maxCodigo = this.livros.reduce((max, l) => Math.max(max, l.codigo), 0);
    livro.codigo = maxCodigo + 1;
    this.livros.push(livro);
  }

  excluir(codigo: number): void {
    const index = this.livros.findIndex(l => l.codigo === codigo);
    if (index >= 0) {
      this.livros.splice(index, 1);
    }
  }
}

import { Editora } from '../model/Editora';

const editoras: Array<Editora> = [
  new Editora(1, 'Alta Books'),
  new Editora(2, 'Pearson'),
  new Editora(3, 'Addison Wesley')
];

export class ControleEditora {
  getEditoras(): Array<Editora> {
    return editoras;
  }

  getNomeEditora(codEditora: number): string {
    const result = editoras.filter(e => e.codEditora === codEditora);
    return result.length > 0 ? result[0].nome : '';
  }
}

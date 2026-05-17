// a) Função swap
const swap = (vetor, pos1, pos2) => {
    let temp = vetor[pos1];
    vetor[pos1] = vetor[pos2];
    vetor[pos2] = temp;
};

// b) Função shuffle
const shuffle = (vetor, numTrocas) => {
    for (let i = 0; i < numTrocas; i++) {
        let pos1 = Math.floor(Math.random() * vetor.length);
        let pos2 = Math.floor(Math.random() * vetor.length);
        swap(vetor, pos1, pos2);
    }
};

// c) Função bubble_sort
const bubble_sort = (vetor) => {
    let n = vetor.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                swap(vetor, j, j + 1);
            }
        }
    }
    return vetor;
};

// d) Função selection_sort
const selection_sort = (vetor) => {
    let n = vetor.length;
    for (let i = 0; i < n - 1; i++) {
        let min_idx = i;
        for (let j = i + 1; j < n; j++) {
            if (vetor[j] < vetor[min_idx]) {
                min_idx = j;
            }
        }
        swap(vetor, min_idx, i);
    }
    return vetor;
};

// f) Função particionamento
const particionamento = (vetor, pos_inicial, pos_final, pivot) => {
    let i = pos_inicial - 1;
    for (let j = pos_inicial; j < pos_final; j++) {
        if (vetor[j] < pivot) {
            i++;
            swap(vetor, i, j);
        }
    }
    swap(vetor, i + 1, pos_final);
    return i + 1;
};

// e) Função quick_sort
const quick_sort = (vetor, pos_inicial, pos_final) => {
    if (pos_inicial < pos_final) {
        let pivot = vetor[pos_final];
        let pi = particionamento(vetor, pos_inicial, pos_final, pivot);
        quick_sort(vetor, pos_inicial, pi - 1);
        quick_sort(vetor, pi + 1, pos_final);
    }
    return vetor;
};

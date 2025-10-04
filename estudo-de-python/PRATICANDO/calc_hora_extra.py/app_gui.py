import tkinter as tk
from tkinter import messagebox
import horas_extras as he

def caucular():
    try:
        salario_base = float(entry_salario.get())
        valor_hora = float(entry_valor_hora.get())
        percentual_desconto = float(entry_percentual.get()) /100
        desconto_fixo = float(entry_desconto_fixo.get())

        sabados_trabalhados = int(entry_sabados_trabalhados.get())
        domingos_trabalhados = int(entry_domingos_tranalhados.get())
        horas_por_sabado = float(entry_horas_sabado.get())
        horas_por_domingo = float(entry_horas_domingo.get())

        total_extras_bruto = he.calc_bruto_hora_extra(
            sabados_trabalhados * horas_por_sabado,
            domingos_trabalhados * horas_por_domingo,
            valor_hora
        )

        resultado = he.calc_salario_liq(
            salario_base,
            total_extras_bruto,
            percentual_desconto,
            desconto_fixo
        )

        resultado_texto = (
            f'Slário base: R$ {salario_base:.2f}\n'
            f'horas extras (bruto): R$ {total_extras_bruto:.2f}\n'
            f"Salário bruto total: R$ {resultado['salario_bruto_total']:.2f}\n"
            f"Descontos totais: R$ {resultado['descontos_totais']:.2f}\n"
            f"Salario liquído final: R$ {resultado['salario_liquido_final']:.2f}"
        )

        messagebox.showinfo('Resultado', resultado_texto)


    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira valores numéricos válidos')


janela = tk.Tk()
janela.title('Calculadora de sálario com horas extras')
janela.geometry('420x520')
janela.resizable(False, False)


tk.Label(janela, text='Sálario base (R$):').pack()
entry_salario = tk.Entry(janela)
entry_salario.pack()


tk.Label(janela, text='Valor da hora normal (R$):').pack()
entry_valor_hora = tk.Entry(janela)
entry_valor_hora.pack()


tk.Label(janela, text='Perentual de desconto (%):').pack()
entry_percentual = tk.Entry(janela)
entry_percentual.pack()


tk.Label(janela, text='Desconto fixo (R$):').pack()
entry_desconto_fixo = tk.Entry(janela)
entry_desconto_fixo.pack()


tk.Label(janela, text='---Horas Extras---').pack()


tk.Label(janela, text='Sabados trabalhados:').pack()
entry_sabados_trabalhados = tk.Entry(janela)
entry_sabados_trabalhados.pack()


tk.Label(janela, text=' Domingos trabalhados:').pack()
entry_domingos_tranalhados = tk.Entry(janela)
entry_domingos_tranalhados.pack()


tk.Label(janela, text='Horas por sabado:').pack()
entry_horas_sabado = tk.Entry(janela)
entry_horas_sabado.pack()


tk.Label(janela, text='Horas por domingo:').pack()
entry_horas_domingo = tk.Entry(janela)
entry_horas_domingo.pack()


tk.Button(janela, text='Calcular', command=caucular, bg='green', fg='white').pack(pady=20)
janela.mainloop()

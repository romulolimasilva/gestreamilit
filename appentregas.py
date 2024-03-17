import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title('Gestao de Entregas')

# Dados dos carros
carro = {
    'carro1':  10, 'carro2': 16, 'carro3': 25, 'carro4': 28, 'carro5': 30, 'carro6': 35, 'carro7': 40, 'carro8': 45, 'carro9': 50, 'carro10': 55
}

# Entregas planejadas
entregas_planejadas = {
     'carro1':  10, 'carro2': 16, 'carro3': 25, 'carro4': 28, 'carro5': 30, 'carro6': 35, 'carro7': 40, 'carro8': 45, 'carro9': 50, 'carro10': 55
}

# Entregas realizadas
entregas_realizadas = {
     'carro1':  9, 'carro2': 15, 'carro3': 25, 'carro4': 28, 'carro5': 30, 'carro6': 25, 'carro7': 38, 'carro8': 9, 'carro9': 1, 'carro10': 54
}

# Entregas devolvidas
entregas_devolvidas = {
    'carro1':  1, 'carro2': 1, 'carro3': 0, 'carro4': 0, 'carro5': 0, 'carro6': 0, 'carro7': 2, 'carro8': 2, 'carro9': 3, 'carro10': 1
}


# Calcular eficiência de entrega
eficiencia_entrega = {carro: (entregas_realizadas[carro] / entregas_planejadas[carro]) * 100 for carro in carro}

# Criar DataFrame para os dados
df = pd.DataFrame({
    'Carro': list(carro.keys()),
    'Entregas Planejadas': list(entregas_planejadas.values()),
    'Entregas Realizadas': list(entregas_realizadas.values()),
    'Entregas Devolvidas': list(entregas_devolvidas.values()),
    'Eficiência de Entrega (%)': list(eficiencia_entrega.values())
})

# Exibindo DataFrame
st.write(df)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
barWidth = 0.2
r1 = range(len(carro))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.bar(r1, df['Entregas Planejadas'], color='blue', width=barWidth, edgecolor='grey', label='Entregas Planejadas')
plt.bar(r2, df['Entregas Realizadas'], color='green', width=barWidth, edgecolor='grey', label='Entregas Realizadas')
plt.bar(r3, df['Entregas Devolvidas'], color='red', width=barWidth, edgecolor='grey', label='Entregas Devolvidas')
plt.bar(r4, df['Eficiência de Entrega (%)'], color='orange', width=barWidth, edgecolor='grey', label='Eficiência de Entrega (%)')

plt.xlabel('Carros')
plt.ylabel('Quantidade de Entregas / Eficiência de Entrega (%)')
plt.title('Entregas Planejadas, Realizadas, Devolvidas e Eficiência de Entrega por Veículo')
plt.xticks([r + barWidth for r in range(len(carro))], list(carro.keys()))
plt.legend()

# Exibindo o gráfico
st.pyplot(plt)

# Botão para gerar relatório
if st.button('Gerar Relatório'):
    st.dataframe(df)
    # Gerando o PDF com o relatório
    df.to_excel('relatorio.xlsx', index=False)
    st.write('Relatório gerado com sucesso!')
    


    


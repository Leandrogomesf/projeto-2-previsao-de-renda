import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Análise de previsão de renda",
     page_icon="https://www.institutots.com.br/wp-content/uploads/2019/12/money-lover-app.png",
     layout="wide",
)

# SIDEBAR configurations

st.sidebar.write("# Seja bem-vindo!")

st.sidebar.write('Para obter informações detalhadas, por favor, realize o login. :red[Isto é só um teste!]')
with st.sidebar:
    with st.form(key='my_form'):
        username = st.text_input('Usuário')
        password = st.text_input('senha')
        st.form_submit_button('Login')
    st.markdown("O objetivo desta análise é prever a variação de renda dos clientes de uma instituição financeira. Os dados utilizados na análise e previsão foram coletados e distribuidos em variáveis com características diversas que auxiliam na previsão ou explicação da renda de um cliente.")

# tabs configuration

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home" 
                                        ,"Gráficos customizáveis" 
                                        ,"Univariadas" 
                                        ,"Bivariadas"
                                        ,"Dados brutos"]
                                        )

with tab1:
    
    renda = pd.read_csv('./input/previsao_de_renda.csv')
    st.title('Análise exploratória da :blue[Previsão de Renda]')
    st.markdown('#### Aqui você encontra informações referentes aos estudos de previsão de renda')
    st.image("https://vibratto.com.br/wpress/wp-content/uploads/2020/01/faturamento-clientes-empresa-neg%C3%B3cio-01.png")
    st.markdown("##### O objetivo desta análise é prever a variação de renda dos clientes de uma instituição financeira. Os dados utilizados na análise e previsão foram coletados e distribuidos em variáveis com características diversas que auxiliam na previsão ou explicação da renda de um cliente.")

    

with tab2:
    
    renda = pd.read_csv('./input/previsao_de_renda.csv')

    #Gráfico customizável univariadas

    st.write('# Gráfico customizável para análises univariadas')
    option1 = st.selectbox(
        'Selecione a variável que deseja exibir',
        ('sexo', 'posse_de_veiculo', 'posse_de_imovel', 
         'qtd_filhos', 'tipo_renda', 'educacao', 
         'estado_civil', 'tipo_residencia', 'idade', 
         'tempo_emprego', 'qt_pessoas_residencia')
        )
    
    fig = plt.figure(figsize=(10, 5))
    sns.lineplot(x='data_ref',y='renda', hue= option1 ,data=renda)
    plt.xlabel(option1)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    #Gráfico customizável bivariadas
    
    st.divider()

    options = st.multiselect(
        'Selecione até duas variáveis que deseja cruzar',
        ['renda','sexo', 'posse_de_veiculo', 'posse_de_imovel', 
        'qtd_filhos', 'tipo_renda', 'educacao', 
        'estado_civil', 'tipo_residencia', 'idade', 
        'tempo_emprego', 'qt_pessoas_residencia'],
        ['educacao', 'renda']
        )
    
    st.write('# Gráfico customizável para análises bivariadas')
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=options[0],y=options[1],data=renda)
    plt.xticks(rotation=30)
    st.pyplot(plt)

with tab3:

    #plots
    
    st.write('# Gráficos ao longo do tempo')
    st.divider()
    fig, ax = plt.subplots(6,1,figsize=(10,40))
    sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[0])
    ax[0].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[1])
    ax[1].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[2])
    ax[2].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[3])
    ax[3].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[4])
    ax[4].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[5])
    ax[5].tick_params(axis='x', rotation=45)
    sns.despine()
    st.pyplot(plt)
     
with tab4:   

    st.write('# Gráficos das análises bivariadas')
    st.divider()
    fig, ax = plt.subplots(7,1,figsize=(10,40))
    sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
    sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
    sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
    sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
    sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
    ax[4].tick_params(axis='x', rotation=20)
    sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
    sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
    ax[6].tick_params(axis='x', rotation=30)
    sns.despine()
    st.pyplot(plt)

with tab5:
    st.markdown("<h1 style='text-align: center; '>Dicionário de dados</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        | Variável                | Descrição                                           | Tipo         |
        | ----------------------- |:---------------------------------------------------:| ------------:|
        | data_ref                |  Data de referência da coleta do dado               | texto|
        | id_cliente              |  Número de identificação do cliente                 | inteiro|
        | sexo                    |  M = 'Masculino'; F = 'Feminino'                    | inteiro|
        | posse_de_veiculo        |  True = 'possui'; False = 'não possui'              | booleana|
        | posse_de_imovel         |  True = 'possui'; False = 'não possui'              | booleana|
        | qtd_filhos              |  Quantidade de filhos do cliente                    | inteiro|
        | tipo_renda              |  Tipo de renda (ex: assaliariado, autônomo etc)     | texto|
        | educacao                |  Nível educacional (ex: secundário, superior etc)   | texto|
        | estado_civil            |  Estado civil (ex: solteiro, casado etc)            | texto|
        | tipo_residencia         |  Tipo de residência (ex: casa/apartamento, com os pais etc)| texto|
        | idade                   |  Idade em anos                                      | inteiro|
        | tempo_emprego           |  Tempo de emprego em anos                           | float|
        | qt_pessoas_residencia   |  Quantidade de pessoas na residência                | float|
        | renda                   |  Valor da renda mensal                              | float|
    """
    )
    st.divider()
    st.markdown("<h1 style='text-align: center; '>Base de dados</h1>", unsafe_allow_html=True)
    st.write(renda)


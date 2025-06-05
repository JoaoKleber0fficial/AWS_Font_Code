import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")
st.title("📊 Dashboard Financeiro com Streamlit")

# === Carrega os dados com separador correto e tratamento de colunas ===
@st.cache_data
def load_data():
    try:
        # Lê CSV com separador ';' e ignora linhas corrompidas
        df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
        df.columns = df.columns.str.strip()  # Remove espaços dos nomes das colunas

        if "Date" not in df.columns:
            st.error("❌ A coluna 'Date' não foi encontrada no CSV.")
            st.stop()

        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Ano-Mês"] = df["Date"].dt.to_period("M").astype(str)

        return df

    except Exception as e:
        st.error(f"Erro ao carregar o CSV: {e}")
        st.stop()

df = load_data()

# === Filtro lateral por país ===
st.sidebar.title("Filtros")
paises = df["Country"].dropna().unique()
pais_escolhido = st.sidebar.selectbox("Selecione um país", sorted(paises))
df_filtrado = df[df["Country"] == pais_escolhido]

st.markdown(f"### 🌍 País selecionado: **{pais_escolhido}**")

# === Receita por Segmento ===
st.markdown("#### 💰 Receita por Segmento")
if "Sales" in df.columns and "Segment" in df.columns:
    receita_segmento = df_filtrado.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
    st.bar_chart(receita_segmento)
else:
    st.warning("Colunas 'Segment' ou 'Sales' não encontradas.")

# === Receita ao Longo do Tempo ===
st.markdown("#### 📈 Receita ao Longo do Tempo")
if "Sales" in df.columns and "Ano-Mês" in df.columns:
    receita_tempo = df_filtrado.groupby("Ano-Mês")["Sales"].sum()
    st.line_chart(receita_tempo)
else:
    st.warning("Colunas 'Sales' ou 'Ano-Mês' não encontradas.")

# === Top 10 Produtos por Receita ===
st.markdown("#### 🏆 Top 10 Produtos por Receita")
if "Product" in df.columns and "Sales" in df.columns:
    top_produtos = df_filtrado.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_produtos)
else:
    st.warning("Colunas 'Product' ou 'Sales' não encontradas.")


# === Mostrar dados brutos ===
with st.expander("🔍 Ver dados brutos"):
    st.dataframe(df_filtrado)

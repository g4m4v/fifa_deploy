import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_jogadores = df_data[(df_data["Club"] == club)]
jogdores = df_jogadores["Name"].value_counts().index
jogador = st.sidebar.selectbox("Jogador", jogdores)

jogador_stats = df_data[df_data["Name"] == jogador].iloc[0]

st.image(jogador_stats["Photo"])
st.title(jogador_stats["Name"])

st.markdown(f"**Clube:** {jogador_stats['Club']}")
st.markdown(f"**Posição:** {jogador_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {jogador_stats['Age']}")
col2.markdown(f"**Altura:** {jogador_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {jogador_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {jogador_stats['Overall']}")
st.progress(int(jogador_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {jogador_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {jogador_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {jogador_stats['Release Clause(£)']:,}")



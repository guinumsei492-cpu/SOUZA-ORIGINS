import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="SOUZA BRAND | Streetwear", page_icon="⚡", layout="wide")

# CSS para Estética Dark & High-End
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;700&display=swap');
    
    .main { background-color: #050505; color: white; font-family: 'Inter', sans-serif; }
    .stApp { background-color: #050505; }
    
    h1 { font-family: 'Bebas Neue', cursive; letter-spacing: 10px; font-size: 70px !important; text-align: center; color: white; margin-bottom: 0px; text-shadow: 2px 2px #333; }
    .subtitle { text-align: center; color: #888; text-transform: uppercase; letter-spacing: 5px; font-size: 14px; margin-bottom: 50px; }
    
    .secao-titulo { font-family: 'Bebas Neue'; font-size: 40px; color: #fff; border-bottom: 2px solid #fff; display: inline-block; margin: 40px 0 20px 0; letter-spacing: 3px; }
    
    .produto-card {
        background-color: #0c0c0c;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #1a1a1a;
        transition: 0.4s ease-in-out;
    }
    .produto-card:hover { border-color: #fff; background-color: #111; }
    
    .preco { color: #fff; font-size: 28px; font-weight: 700; margin: 10px 0; font-family: 'Bebas Neue'; }
    
    .botao-comprar {
        background: white;
        color: black !important;
        font-weight: bold;
        text-align: center;
        padding: 14px;
        border-radius: 4px;
        display: block;
        text-decoration: none;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 14px;
    }
    .botao-comprar:hover { background: #f0f0f0; box-shadow: 0px 0px 15px rgba(255,255,255,0.3); }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. Banco de Dados do Drop 01 (Camiseta, Calça e Conjunto)
if 'produtos' not in st.session_state:
    st.session_state.produtos = [
        {
            "cat": "SETS (KITS)",
            "nome": "CONJUNTO SYNA WORLD - TRACKSUIT SUMMER", 
            "preco": 289.90, 
            "img": "https://cf.shopee.com.br/file/br-11134207-7qukw-ljm3o2z8f7mf9d", # Imagem do conjunto Syna
            "desc": "Kit Camiseta + Bermuda Moletom | Estilo Gringo Premium | Logo Bordado",
            "tamanhos": ["P", "M", "G", "GG"]
        },
        {
            "cat": "TOPS (CAMISETAS)",
            "nome": "T-SHIRT 'BLESSED ANGELS' OVERSIZED", 
            "preco": 149.90, 
            "img": "https://cf.shopee.com.br/file/br-11134207-7qukw-ljm3o3288888f1",
            "desc": "100% Algodão Premium | High Definition Print",
            "tamanhos": ["P", "M", "G", "GG"]
        },
        {
            "cat": "BOTTOMS (CALÇAS)",
            "nome": "JEANS BAGGY 'NIGHT' ESTONADO", 
            "preco": 219.90, 
            "img": "https://cf.shopee.com.br/file/br-11134207-7r98o-lzp6b66t6666e1",
            "desc": "Denim Baggy Fit | Lavagem Estonada Industrial",
            "tamanhos": ["38", "40", "42", "44", "46"]
        }
    ]

# 3. Cabeçalho Principal
st.markdown("<h1>SOUZA BRAND</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>The New Era of Brazilian Streetwear</p>", unsafe_allow_html=True)

# 4. Exibição Dinâmica por Categorias
categorias = ["SETS (KITS)", "TOPS (CAMISETAS)", "BOTTOMS (CALÇAS)"]

for cat in categorias:
    itens = [p for p in st.session_state.produtos if p['cat'] == cat]
    if itens:
        st.markdown(f"<div class='secao-titulo'>{cat}</div>", unsafe_allow_html=True)
        cols = st.columns(len(itens) if len(itens) > 1 else 2)
        
        for i, item in enumerate(itens):
            with cols[i]:
                st.markdown(f"""
                <div class="produto-card">
                    <img src="{item['img']}" style="width:100%; border-radius:4px; filter: grayscale(20%);">
                    <h3 style="font-family: 'Bebas Neue'; margin-top:15px; letter-spacing:1px; font-size: 22px;">{item['nome']}</h3>
                    <p style="color: #666; font-size: 12px; height: 30px;">{item['desc']}</p>
                    <p class="preco">R$ {item['preco']:.2f}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Seleção e Compra
                tam = st.selectbox(f"TAMANHO:", item['tamanhos'], key=f"k_{item['nome']}")
                
                link_zap = f"https://wa.me/557182768278?text=Salve%20Souza!%20Quero%20o%20{item['nome']}%20tamanho%20{tam}"
                st.markdown(f'<a href="{link_zap}" target="_blank" class="botao-comprar">RESERVAR PEÇA</a>', unsafe_allow_html=True)
                st.write("")

# 5. Footer
st.write("---")
st.markdown("<p style='text-align: center; color: #444; font-size: 10px; letter-spacing: 3px;'>SOUZA BRAND INTERNATIONAL | ALL RIGHTS RESERVED 2024</p>", unsafe_allow_html=True)

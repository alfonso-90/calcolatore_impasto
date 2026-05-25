import streamlit as st
import math

# Configurazione della pagina dello smartphone
st.set_page_config(page_title="Calcolatore impasti", page_icon="🍕", layout="centered")

# Grafica e Titoli
st.title("🍕 Calcolatori impasti per Rik Velluso")
st.subheader("Sistema Bilanciamento Impasti Professionale")
st.markdown("*Idratazione 73.4% | Biga al 50% idratata*")
st.divider()

# Input con uno slider comodo per lo smartphone
farina_totale_req = st.slider("Quanti KG di FARINA TOTALE vuoi impastare oggi?", min_value=1.0, max_value=100.0, value=50.0, step=0.5)

# --- I TUOI PARAMETRI REALI ---
percentuale_farina_biga = 0.30 
idratazione_biga = 0.50          
idratazione_totale = 0.734       
lievito_per_kg_farina_biga = 2.083  
lievito_rinfresco_per_kg_totale = 0.4 
percentuale_sale = 0.025         

# --- CALCOLO STEP 1: LA BIGA ---
farina_biga = farina_totale_req * percentuale_farina_biga
acqua_biga = farina_biga * idratazione_biga
lievito_biga = farina_biga * lievito_per_kg_farina_biga
peso_totale_biga = farina_biga + acqua_biga + (lievito_biga / 1000)

# --- CALCOLO STEP 2: IL RINFRESCO ---
farina_rinfresco = farina_totale_req - farina_biga
acqua_totale = farina_totale_req * idratazione_totale
acqua_rinfresco = acqua_totale - acqua_biga
sale_totale = farina_totale_req * percentuale_sale
lievito_rinfresco = farina_totale_req * lievito_rinfresco_per_kg_totale

peso_finale_impasto = farina_totale_req + acqua_totale + sale_totale + ((lievito_biga + lievito_rinfresco)/1000)
panetti_stimati = (peso_finale_impasto * 1000) / 280

# --- MOSTRA I RISULTATI SULLO SCHERMO ---

st.header("🦁 1. LA BIGA (Il giorno prima)")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🌾 Farina", f"{round(farina_biga, 2)} kg")
with col2:
    st.metric("💧 Acqua (50%)", f"{round(acqua_biga, 2)} lt")
with col3:
    st.metric("🧫 Lievito", f"{round(lievito_biga, 1)} gr")
st.info(f"👉 **Peso totale biga da pesare l'indomani:** {round(peso_totale_biga, 2)} kg")

st.divider()

st.header("🌀 2. IL RINFRESCO (Impasto finale)")
st.caption("Metti nella vasca tutta la biga del giorno prima e aggiungi:")
col4, col5, col6, col7 = st.columns(4)
with col4:
    st.metric("🌾 Farina Nuova", f"{round(farina_rinfresco, 2)} kg")
with col5:
    st.metric("💧 Acqua Nuova", f"{round(acqua_rinfresco, 2)} lt")
with col6:
    st.metric("🧂 Sale", f"{int(sale_totale * 1000)} gr")
with col7:
    st.metric("🧫 Lievito Nuov", f"{round(lievito_rinfresco, 1)} gr")

st.divider()

# Resoconto Finale della Massa
st.success(f"📈 **Massa totale in uscita:** {round(peso_finale_impasto, 2)} kg | 🍕 **Panetti stimati (~250g):** {math.floor(panetti_stimati)} pz")

st.caption("💡 *Consiglio di Bruno: Spezza la biga a pezzetti nell'acqua del rinfresco prima di aggiungere la farina!*")

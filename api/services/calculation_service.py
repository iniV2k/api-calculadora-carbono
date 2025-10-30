from api.data import fatores_emissao


FATORES_EMISSAO = fatores_emissao.fatoresEmissao()

GRAMAS_POR_COLHER_ARROZ = 20
GRAMAS_POR_COLHER_FEIJAO = 25
GRAMAS_POR_KG = 1000
DIAS_POR_ANO = 365.25

def calcular_pegada_carbono(data: dict) -> dict:
    transporte_data = data.get("transporte", {})
    alimentacao_data = data.get("alimentacao", {})
    moradia_data = data.get("moradia", {})
    emissores = []
    
    gramas_arroz_dia = alimentacao_data.get("arroz", 0) * GRAMAS_POR_COLHER_ARROZ
    gramas_feijao_dia = alimentacao_data.get("feijao", 0) * GRAMAS_POR_COLHER_FEIJAO
    
    kg_arroz_anual = (gramas_arroz_dia * DIAS_POR_ANO) / GRAMAS_POR_KG
    kg_feijao_anual = (gramas_feijao_dia * DIAS_POR_ANO) / GRAMAS_POR_KG
    
    co2_gasolina = transporte_data.get("gasolina", 0) * FATORES_EMISSAO["transporte"]["gasolina"] * 12
    co2_diesel = transporte_data.get("diesel", 0) * FATORES_EMISSAO["transporte"]["diesel"] * 12
    co2_etanol = transporte_data.get("etanol", 0) * FATORES_EMISSAO["transporte"]["etanol"] * 12
    co2_gnv = transporte_data.get("gnv", 0) * FATORES_EMISSAO["transporte"]["gnv"] * 12
    co2_voo_dom = transporte_data.get("vooDomestico", 0) * FATORES_EMISSAO["transporte"]["vooDomestico"]
    co2_voo_int = transporte_data.get("vooInternacional", 0) * FATORES_EMISSAO["transporte"]["vooInternacional"] 
    emissores.extend([
        {"nome": "Gasolina", "co2": co2_gasolina},
        {"nome": "Diesel", "co2": co2_diesel},
        {"nome": "Etanol", "co2": co2_etanol},
        {"nome": "GNV", "co2": co2_gnv},
        {"nome": "Voo Doméstico", "co2": co2_voo_dom},
        {"nome": "Voo Internacional", "co2": co2_voo_int},
    ])
    total_co2_transporte = co2_gasolina + co2_diesel + co2_etanol + co2_gnv + co2_voo_dom + co2_voo_int
    
    co2_carne_bovina = alimentacao_data.get("carneBovina", 0) * FATORES_EMISSAO["alimentacao"]["carneBovina"] * 52
    co2_carne_suina = alimentacao_data.get("carneSuina", 0) * FATORES_EMISSAO["alimentacao"]["carneSuina"] * 52
    co2_carne_frango = alimentacao_data.get("carneFrango", 0) * FATORES_EMISSAO["alimentacao"]["carneFrango"] * 52
    co2_ovos = alimentacao_data.get("ovos", 0) * FATORES_EMISSAO["alimentacao"]["ovos"] * 52
    co2_arroz = kg_arroz_anual * FATORES_EMISSAO["alimentacao"]["arroz"]
    co2_feijao = kg_feijao_anual * FATORES_EMISSAO["alimentacao"]["feijao"]
    
    emissores.extend([
        {"nome": "Carne Bovina", "co2": co2_carne_bovina},
        {"nome": "Carne Suína", "co2": co2_carne_suina},
        {"nome": "Carne de Frango", "co2": co2_carne_frango},
        {"nome": "Arroz", "co2": co2_arroz},
        {"nome": "Feijão", "co2": co2_feijao},
        {"nome": "Ovos", "co2": co2_ovos},
    ])
    total_co2_alimentacao = co2_carne_bovina + co2_carne_suina + co2_carne_frango + co2_arroz + co2_feijao + co2_ovos
    
    total_moradores = moradia_data.get("moradores", 1)
    co2_efluentes = total_moradores * FATORES_EMISSAO["moradia"]["efluentes_per_capita"]
    co2_eletricidade = moradia_data.get("kWh", 0) * FATORES_EMISSAO["moradia"]["kWh"] * 12
    co2_lixo = moradia_data.get("lixoComum", 0) * FATORES_EMISSAO["moradia"]["lixoComum"] * 12
    co2_gas_botijao = moradia_data.get("gasBotijao", 0) * FATORES_EMISSAO["moradia"]["gasBotijao"] * 12
    co2_gas_encanado = moradia_data.get("gasEncanado", 0) * FATORES_EMISSAO["moradia"]["gasEncanado"] * 12
    emissores.extend([
        {"nome": "Eletricidade", "co2": co2_eletricidade},
        {"nome": "Lixo", "co2": co2_lixo},
        {"nome": "Gás de Botijão", "co2": co2_gas_botijao},
        {"nome": "Gás Encanado", "co2": co2_gas_encanado},
        {"nome": "Efluentes", "co2": co2_efluentes},
    ])
    total_co2_moradia = co2_eletricidade + co2_lixo + co2_gas_botijao + co2_gas_encanado + co2_efluentes
    
    total_co2_anual = total_co2_transporte + total_co2_alimentacao + total_co2_moradia
    
    emissores_filtrados = [e for e in emissores if e["co2"] > 0]
    top_emitter = sorted(emissores_filtrados, key=lambda item: item["co2"], reverse=True)
    
    response_data = {
        "totalCo2": total_co2_anual,
        "breakdown": {
            "transporte": {
                "total": total_co2_transporte, 
                "gasolinaCo2": co2_gasolina,
                "dieselCo2": co2_diesel,
                "etanolCo2": co2_etanol,
                "gnvCo2": co2_gnv,
                "vooDomesticoCo2": co2_voo_dom,
                "vooInternacionalCo2": co2_voo_int},
            "alimentacao": {
                "total": total_co2_alimentacao, 
                "carneBovinaCo2": co2_carne_bovina,
                "carneSuinaCo2": co2_carne_suina,
                "carneFrangoCo2": co2_carne_frango,
                "arrozCo2": co2_arroz,
                "feijaoCo2": co2_feijao,
                "ovosCo2": co2_ovos},
            "moradia": {
                "total": total_co2_moradia, 
                "eletricidadeCo2": co2_eletricidade,
                "lixoComumCo2": co2_lixo,
                "efluentesCo2": co2_efluentes,
                "gasBotijaoCo2": co2_gas_botijao,
                "gasEncanadoCo2": co2_gas_encanado}
        },
        "topEmitters": top_emitter[:3]
    }
    return response_data
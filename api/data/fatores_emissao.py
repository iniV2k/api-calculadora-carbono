def fatoresEmissao():
    FATORES_EMISSAO = {
            "transporte": {
                "gasolina": 2.3,
                "diesel": 3.2,
                "etanol": 0.78,
                "gnv": 1.66,
                "vooDomestico": 106.1,
                "vooInternacional": 605.6
            }, "moradia": {
                "kWh": 0.1,
                "lixoComum": 1,
                "efluentes_per_capita": 45,
                "gasBotijao": 2.99,
                "gasEncanado": 1.99,
            }, "alimentacao": {
                "carneBovina": 152.1,
                "carneSuina": 5.2,
                "carneFrango": 0.6,
                "arroz": 1.5,
                "feijao": 0.9,
                "ovos": 0.1
            }
        }
    return FATORES_EMISSAO
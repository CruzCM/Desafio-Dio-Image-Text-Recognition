import os
from PIL import Image
import pytesseract

pasta_entrada = 'inputs'
pasta_saida = 'output'
imagens = os.listdir(pasta_entrada)

for nome_imagem in imagens:
    try:
        
        caminho_imagem = os.path.join(pasta_entrada, nome_imagem)

        with Image.open(caminho_imagem) as img:
            texto = pytesseract.image_to_string(img)
        
        arquivo_saida = os.path.join(pasta_saida, f"{os.path.splitext(nome_imagem)[0]}.txt")

        with open(arquivo_saida, 'w') as f:
            f.write(texto)

        print(f"Processado {nome_imagem} com sucesso.")
    
    except Exception as e:
        print(f"Erro ao processar {nome_imagem}: {e}")

print("Processo de OCR concluído. Resultados salvos na pasta 'output'.")

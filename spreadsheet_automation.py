import openai
import pandas as pd

openai.api_key = "(inserir key da api valida)"

#caminho da pasta
df = pd.read_excel('C:/Users/jonas/Downloads/fitness_exercises_limpo.xlsx')

# Para cada nome de exercício na coluna 'name', usando API automaticamente
for i, name in enumerate(df['name']):
    description = df.loc[i, 'description']
    
    # Verificando se a descrição está vazia, caso esteja, preenche
    if pd.isna(description) or not description.strip():
        prompt = f"Descreva como realizar o exercício '{name}' em até 30 palavras. Certifique-se de incluir os músculos trabalhados e dicas para a execução correta, sem tópicos, explicando de maneira descritiva."
        print(f"Descreva como realizar o exercício '{name}' em até 30 palavras. Certifique-se de incluir os músculos trabalhados e dicas para a execução correta.")
        response = openai.Completion.create(
            engine="text-davinci-001", prompt=prompt, max_tokens=100
        )

        new_description = ".".join(response.choices[0].text.strip().split(".")[:-1]).strip()
        print('\n', new_description)

        df.loc[i, 'description'] = new_description

#Salvar planilha 
df.to_excel('C:/Users/jonas/Downloads/Documentos/fitness_exercises_limpo.xlsx', index=False)
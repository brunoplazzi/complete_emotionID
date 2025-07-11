# EmotionID


> **⚠️ Requisito obrigatório:**  
> Este projeto exige a versão do **Python 3.10.9**. Certifique-se de que ela está instalada antes de continuar.\n
> Este projeto exige a versão do **Node 22.17.X (última versão estável)**. Certifique-se de que ela está instalada antes de continuar.
> 
> **💡 Observação:**  
> Este guia é voltado para usuários **Windows**. Em sistemas Linux, a estrutura de instalação é semelhante, mas os comandos de ativação de ambiente virtual e scripts podem variar.

---

## 📦 Como instalar o projeto


### ✅ Opção 1: Instalação automática com script (Recomendada)

1. **Baixe o projeto** para seu computador (clonando via Git ou baixando como `.zip` e extraindo).
2. **Execute o script `setup.bat`** localizado na raiz do projeto:
   - Clique duas vezes no arquivo `setup.bat`, **ou**
   - Execute pelo terminal:
     
     ```cmd
     setup.bat
     ```

3. O script irá:
   - Criar e ativar o ambiente virtual do backend.
   - Instalar as dependências necessárias.
   - Iniciar o backend.
   - Instalar as dependências do frontend.
   - Iniciar o frontend.
   - Abrir automaticamente o navegador com o sistema rodando em `http://localhost:5173`.

> Após a execução, o projeto estará funcionando localmente e pronto para uso. 🎉

---

### ✅ Opção 2: Instalação manual (passo a passo)

---

#### 🔙 Backend

1. Acesse a pasta `backend`:
   ```cmd
   cd backend
   ```

2. **Crie o ambiente virtual** (caso ainda não exista):
   ```cmd
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:
   ```cmd
   venv\Scripts\activate
   ```

4. **Instale as dependências**:
   ```cmd
   pip install -r requirements.txt
   ```

5. **Inicie o servidor backend**:
   ```cmd
   uvicorn app.main:app --reload
   ```

> O backend estará rodando em `http://127.0.0.1:8000`.

---

#### 🔜 Frontend

1. Em outro terminal, volte à raiz do projeto (caso ainda esteja em `backend`) e acesse a pasta `frontend`:
   ```cmd
   cd ../frontend
   ```

2. **Instale as dependências** (caso ainda não existam):
   ```cmd
   npm install
   ```

3. **Inicie o servidor de desenvolvimento**:
   ```cmd
   npm run dev
   ```

> O frontend será iniciado em `http://localhost:5173`.

---

### 🌐 Acessando o sistema

Com ambos os servidores (backend e frontend) em execução, abra seu navegador e acesse:

```
http://localhost:5173
```

O sistema estará disponível para uso!


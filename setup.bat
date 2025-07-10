@echo off
setlocal

echo ================================
echo Iniciando o projeto completo...
echo ================================

REM === BACKEND SETUP ===
echo.
echo === Preparando o backend ===
cd backend

if not exist venv (
    echo Criando ambiente virtual...
    python -m venv venv
) else (
    echo Ambiente virtual já existe.
)

echo Ativando o ambiente virtual...
call venv\Scripts\activate

echo Instalando dependências do backend...
pip install -r requirements.txt

echo Iniciando o backend...
start cmd /k "call venv\Scripts\activate && uvicorn app.main:app --reload"

cd ..

REM === FRONTEND SETUP ===
echo.
echo === Preparando o frontend ===
cd frontend

if not exist node_modules (
    echo Instalando dependências do frontend...
    npm install
) else (
    echo Dependências do frontend já instaladas.
)

echo Iniciando o frontend...
start cmd /k "npm run dev"

cd ..

REM === ABRIR NAVEGADOR ===
echo.
echo Abrindo o site no navegador...
start "" "http://localhost:5173"

echo.
echo Projeto iniciado com sucesso!
pause

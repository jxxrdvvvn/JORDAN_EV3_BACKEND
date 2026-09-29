@echo off
echo ===================================================
echo   RESTAURANDO DEPENDENCIAS DEL PROYECTO - ES3
echo ===================================================
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.
echo ===================================================
echo   INSTALACION COMPLETADA CON EXITO
echo ===================================================
pause
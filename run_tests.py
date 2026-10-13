import subprocess
import sys

def main():
    print("=" * 60)
    print("EJECUCIÓN DE PRUEBAS UNITARIAS Y ANÁLISIS DE COBERTURA")
    print("=" * 60)
    
    # 1. Ejecutar las pruebas unitarias existentes del proyecto Django midiendo cobertura
    test_cmd = [
        sys.executable, "-m", "coverage", "run",
        "--source=.",
        "manage.py", "test", "test_autoparts"
    ]
    test_result = subprocess.run(test_cmd)
    
    print("\n" + "=" * 60)
    print("REPORTE DETALLADO DE COBERTURA Y LÍNEAS NO CUBIERTAS")
    print("=" * 60)
    
    # 2. Generar reporte por consola mostrando líneas faltantes (-m / --show-missing)
    report_cmd = [
        sys.executable, "-m", "coverage", "report",
        "-m",
        "--omit=venv/*,manage.py,test_autoparts/*"
    ]
    subprocess.run(report_cmd)
    
    # Si las pruebas fallaron, salir con el código de error correspondiente
    if test_result.returncode != 0:
        print("\n[ALERTA] Se detectaron pruebas unitarias fallidas durante la ejecución.")
        sys.exit(test_result.returncode)

if __name__ == "__main__":
    main()
import re
from collections import Counter

def analyze_log(file_path):
    # Patrón para buscar errores "Failed password" (común en servidores Linux)
    failed_login_pattern = r"Failed password for .* from ([\d\.]+) port"
    
    ips_con_fallos = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                match = re.search(failed_login_pattern, line)
                if match:
                    # Extraemos la dirección IP que intentó entrar
                    ips_con_fallos.append(match.group(1))
        
        # Contamos cuántas veces aparece cada IP
        conteo = Counter(ips_con_fallos)
        
        print("--- Security Log Analysis Report ---")
        if not ips_con_fallos:
            print("[✅] No suspicious failed logins detected.")
        else:
            print("[🚨] Suspicious activity detected!")
            for ip, count in conteo.items():
                if count > 3: # Marcamos como alerta si hay más de 3 fallos
                    print(f"ALERT: IP {ip} failed login {count} times (Potential Brute Force)")
                else:
                    print(f"Info: IP {ip} failed login {count} times")
                    
    except FileNotFoundError:
        print("[!] Error: Log file not found.")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Simulación: En un entorno real, aquí pondrías la ruta al log del servidor
    analyze_log("samples/server_access.log")

#!/usr/bin/env python3
"""
🤖 Extraer Automáticamente desde Web - Auditoría IA CLM

Script automatizado con Selenium para extraer datos de Formspree SIN API KEY.

Requiere:
- pip install selenium
- Chrome/Chromium instalado

Uso:
    python3 extraer_automatico_web.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import sys
import os

class FormspreeExtractor:
    """Extrae datos de Formspree usando Selenium."""

    def __init__(self):
        """Configurar navegador Chrome en modo headless."""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Sin interfaz gráfica
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.submissions = []

    def login(self, email, password):
        """
        Hacer login en Formspree.

        Args:
            email: Email de cuenta Formspree
            password: Contraseña
        """
        print("🔐 Haciendo login...")

        self.driver.get("https://formspree.io/login")

        # Ingresar email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)

        # Ingresar password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        # Click en login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Esperar a que cargue el dashboard
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("dashboard")
        )

        print("✅ Login exitoso")

    def ir_a_formulario(self, form_id='mjgalypd'):
        """Ir al formulario específico."""
        print(f"📋 Navegando al formulario {form_id}...")

        self.driver.get(f"https://formspree.io/forms/{form_id}/submissions")

        # Esperar a que carguen las submissions
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "submissions"))
        )

        print("✅ Formulario cargado")

    def extraer_submissions(self, max_submissions=100):
        """
        Extrae datos de las submissions.

        Args:
            max_submissions: Máximo de submissions a extraer
        """
        print(f"📥 Extrayendo submissions (máx: {max_submissions})...")

        # Encontrar todas las submissions
        submission_elements = self.driver.find_elements(By.CLASS_NAME, "submission-item")

        total_submissions = min(len(submission_elements), max_submissions)

        print(f"📊 Found {len(submission_elements)} submissions, extrayendo {total_submissions}")

        for i, submission_elem in enumerate(submission_elements[:total_submissions]):
            try:
                print(f"   [{i+1}/{total_submissions}] Extrayendo...")

                # Click en la submission
                submission_elem.click()

                # Esperar a que cargue el detalle
                time.sleep(1)

                # Buscar el JSON de la submission
                try:
                    # El JSON suele estar en un elemento <pre> o <code>
                    json_element = self.driver.find_element(By.TAG_NAME, "pre")

                    if json_element:
                        json_text = json_element.text

                        try:
                            data = json.loads(json_text)
                            self.submissions.append(data)
                        except json.JSONDecodeError:
                            # Si no es JSON válido, intentar extraer el reply
                            if 'reply' in json_text:
                                # Buscar el JSON dentro del texto
                                inicio = json_text.find('{')
                                if inicio != -1:
                                    # Encontrar el cierre del JSON
                                    nivel = 0
                                    fin = inicio
                                    for x in range(inicio, len(json_text)):
                                        if json_text[x] == '{':
                                            nivel += 1
                                        elif json_text[x] == '}':
                                            nivel -= 1
                                            if nivel == 0:
                                                fin = x + 1
                                                break

                                    json_str = json_text[inicio:fin]
                                    data = json.loads(json_str)
                                    self.submissions.append(data)

                except Exception as e:
                    print(f"      ⚠️  Error: {e}")

                # Volver atrás
                self.driver.back()

                # Esperar a que cargue la lista
                time.sleep(0.5)

            except Exception as e:
                print(f"   ❌ Error en submission {i+1}: {e}")
                continue

        print(f"✅ Extraídas {len(self.submissions)} submissions")

    def guardar_datos(self, archivo_salida='data/formspree_extraido.json'):
        """Guarda los datos extraídos en formato JSON."""
        os.makedirs('data', exist_ok=True)

        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(self.submissions, f, indent=2, ensure_ascii=False)

        print(f"✅ Datos guardados en: {archivo_salida}")

    def cerrar(self):
        """Cierra el navegador."""
        self.driver.quit()
        print("🔚 Navegador cerrado")

def main():
    """Función principal."""
    print("\n" + "="*60)
    print("🤖 EXTRACCIÓN AUTOMÁTICA DESDE WEB")
    print("="*60)

    extractor = FormspreeExtractor()

    try:
        # Opción 1: Con login
        # email = input("Email de Formspree: ").strip()
        # password = input("Contraseña: ").strip()
        # extractor.login(email, password)

        # Opción 2: Sin login (si ya estás logueado en Chrome)
        print("📝 NOTA: Asegúrate de estar logueado en Formspree en Chrome")
        input("Presiona Enter después de loguearte en Formspree en el navegador...")

        extractor.ir_a_formulario()
        extractor.extraer_submissions(max_submissions=50)
        extractor.guardar_datos()

        print("\n" + "="*60)
        print("✅ EXTRACCIÓN COMPLETADA")
        print("="*60)

        print(f"\n📊 Total submissions extraídas: {len(extractor.submissions)}")

        print(f"\n💡 Ahora puedes analizar los datos:")
        print(f"   python3 scripts/analizar_resultados.py --archivo data/formspree_extraido.json")
        print(f"   python3 scripts/metricas_por_camino.py --archivo data/formspree_extraido.json")

    except KeyboardInterrupt:
        print("\n\n⚠️  Proceso interrumpido por usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        extractor.cerrar()

if __name__ == '__main__':
    main()

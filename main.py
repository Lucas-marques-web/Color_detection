import cv2
import numpy as np

# Dicionário de cores e seus respectivos limites de intervalo no espaço HSV
color_ranges = {
    'vermelho': ([100, 50, 50], [255, 100, 100]),
    'verde': ([50, 100, 50], [100, 255, 100]),
    'azul': ([50, 50, 100], [100, 100, 255])
}

# Inicializar a webcam
cap = cv2.VideoCapture(0)

# Função para pré-processar a imagem
def preprocess_image(frame):
    # Redimensionar a imagem para melhorar o desempenho
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    # Aplicar suavização para reduzir ruídos
    frame_blur = cv2.GaussianBlur(frame, (5, 5), 0)

    return frame_blur

while True:
    # Ler o quadro atual da webcam
    ret, frame = cap.read()

    # Pré-processar a imagem
    frame = preprocess_image(frame)

    # Converter o quadro para o espaço de cores HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Iterar sobre cada cor definida no dicionário
    for color_name, (lower, upper) in color_ranges.items():
        # Criar uma máscara para a cor atual
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

        # Aplicar operações morfológicas para melhorar a forma dos objetos
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Encontrar os contornos dos objetos detectados na máscara
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Verificar se pelo menos um contorno foi encontrado
        if len(contours) > 0:
            # Encontrar o maior contorno (supondo que seja o objeto de interesse)
            max_contour = max(contours, key=cv2.contourArea)

            # Verificar a área do contorno para filtrar pequenos ruídos
            contour_area = cv2.contourArea(max_contour)
            if contour_area > 500:
                # Encontrar o retângulo delimitador do contorno
                x, y, w, h = cv2.boundingRect(max_contour)

                # Desenhar um retângulo em volta do objeto detectado
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Escrever o nome da cor no retângulo
                cv2.putText(frame, color_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Mostrar o quadro com as detecções
    cv2.imshow('Detectar cores', frame)

    # Parar o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
import qrcode
from PIL import Image
import gradio as gr
import io
import base64
import numpy as np
import cv2
import tempfile


# QR kod oluşturma işlevi
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Base64 kodlama
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # PNG olarak geçici kaydetme
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    img.save(temp_file.name, format="PNG")
    temp_file.close()

    return f"data:image/png;base64,{img_base64}", temp_file.name, img_base64




# Gradio arayüzü oluşturma
def create_gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## QR Code Generator ")

        # QR kod oluşturma sekmesi
        with gr.Tab("Generate QR Code"):
            data_input = gr.Textbox(placeholder="Linki girin", label="Link")
            generate_button = gr.Button("Generate QR Code")
            qr_code_html = gr.HTML(label="Generated QR Code (Base64 Embedded)")
            qr_png_file = gr.File(label="Download QR Code (PNG)")
            qr_base64_file = gr.File(label="Download Base64 (TXT)")

            def generate_qr_interface(data):
                if not data.strip():
                    raise ValueError("Input text cannot be empty!")
                img_base64, png_path, base64_str = generate_qr(data)

                base64_txt_path = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
                with open(base64_txt_path.name, "w") as f:
                    f.write(base64_str)

                html_content = f'<img src="{img_base64}" alt="QR Code" style="max-width:300px;">'
                return html_content, png_path, base64_txt_path.name

            generate_button.click(
                generate_qr_interface,
                inputs=data_input,
                outputs=[qr_code_html, qr_png_file, qr_base64_file],
            )


    demo.launch(share=True)


# Arayüzü çalıştırma
create_gradio_interface()

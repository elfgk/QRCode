# QR Code Generator

Bu uygulama, URL veya metin girdisi ile QR kodları oluşturmanızı sağlar. QR kodunu Base64 formatında veya PNG dosyası olarak indirebilirsiniz. Ayrıca, oluşturduğunuz QR kodları görsel olarak da görüntülenebilir.

## Özellikler

- **QR Kod Oluşturma**: URL veya metin girerek QR kodları oluşturun.
- **QR Kod Görüntüleme**: Oluşturduğunuz QR kodunu Base64 formatında entegre edilmiş bir görsel olarak görüntüleyin.
- **QR Kod İndirme**: Oluşturduğunuz QR kodunu PNG dosyası olarak indirebilir veya Base64 formatındaki metni bir `.txt` dosyası olarak kaydedebilirsiniz.

## Kullanım

1. **QR Kodu Oluşturma**:
    - Ana sayfada, "Link" kutusuna QR kodunu oluşturmak için bir metin veya URL girin.
    - "Generate QR Code" butonuna tıklayın.
    - QR kodu, görsel olarak ekranda görüntülenecektir.
    - Ayrıca, QR kodunu **PNG dosyası** olarak veya **Base64 string** olarak indirme seçenekleri de sunulacaktır.

2. **QR Kodu Görüntüleme**:
    - Girilen URL veya metin, QR koda dönüştürülerek ilgili sekmede görselleştirilir.
    - Base64 olarak kodlanmış görsel de aynı şekilde kullanıcıya sunulur.

3. **QR Kodu İndirme**:
    - QR kodunun görselini **PNG dosyası** olarak bilgisayarınıza indirebilirsiniz.
    - Alternatif olarak, **Base64 kodu** bir `.txt` dosyasına kaydedilerek indirilir.

## Gereksinimler

Bu uygulamayı çalıştırmak için aşağıdaki Python paketlerinin yüklü olması gerekir:

- `qrcode`
- `PIL` (Pillow)
- `gradio`
- `numpy`
- `opencv-python`

Gerekli paketleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install qrcode[pil] gradio numpy opencv-python
```

<h1 align="center"> 𓍢ִ໋☕️✧˚ ༘ ⋆ </h1>

<h1> İletişim: </h1>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/elfgk/)
[![Stack Overflow](https://img.shields.io/badge/StackOverflow-FE7A16?style=for-the-badge&logo=stackoverflow&logoColor=white)](https://stackoverflow.com/users/27559679/elfgk)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-9C30FF?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/elfgk)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/elfgkk)

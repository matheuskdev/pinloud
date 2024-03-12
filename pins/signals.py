import os
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image, ImageDraw, ImageFont

from core import settings

from .models import Pin


def draw_image(main_image, instance):
    # Adicione o e-mail do usuário à imagem
    draw = ImageDraw.Draw(main_image)
    # Especifique apenas o tamanho da fonte
    font_size = 12  # Ajuste o tamanho conforme necessário
    font = ImageFont.load_default()
    # Ajuste o tamanho da fonte
    font = font.font_variant(size=font_size)
    # Ajuste a posição conforme necessário
    email_text = f"{instance.user.email} "
    draw.text((10, 30), email_text, font=font, fill=(255, 255, 255))


@receiver(post_save, sender=Pin)
def apply_watermark(sender, instance, created, **kwargs):
    if created:
        watermark_path = os.path.join(
            settings.BASE_DIR, "templates/static/img/Logo_Pinloud_Branca.png"
        )
        watermark = Image.open(watermark_path)

        # Abra a imagem principal
        main_image = Image.open(instance.image)

        # Redimensione a marca d'água conforme necessário
        watermark = watermark.resize((25, 25))

        # Adicione a marca d'água à imagem principal
        main_image.paste(watermark, (10, 10), watermark)

        # Converta a imagem final de volta para um arquivo
        output = BytesIO()
        main_image.save(output, format="PNG")
        output.seek(0)

        # Substitui o arquivo  original pelo novo arquivo com marca d'água
        instance.image = InMemoryUploadedFile(
            output,
            "ImageField",
            f"{instance.image.name.split('.')[0]}_watermarked.png",
            "image/png",
            output.tell(),
            None,
        )

        instance.save()


# Registre o sinal quando o módulo é carregado
signals.post_save.connect(apply_watermark, sender=Pin)
